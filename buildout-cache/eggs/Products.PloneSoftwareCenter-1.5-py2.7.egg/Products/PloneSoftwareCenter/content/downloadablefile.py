"""
$Id: PSCFile.py 19225 2006-02-13 05:50:18Z limi $
"""

import re

from zope.interface import implements

from Products.PloneSoftwareCenter.interfaces import IFileContent

from AccessControl import ClassSecurityInfo
from Products.CMFCore import permissions

from Products.Archetypes.atapi import * 

from Products.PloneSoftwareCenter import config
from Products.ATContentTypes.content.base import ATCTFileContent

# We need to make sure that the right storage is set at Field
# creation to correctly trigger the layer registration process
if config.USE_EXTERNAL_STORAGE:
    from Products.ExternalStorage.ExternalStorage import ExternalStorage
    downloadableFileStorage = ExternalStorage(
        prefix=config.EXTERNAL_STORAGE_PATH,
        archive=False,
        rename=False,
    )
else:
    downloadableFileStorage = AttributeStorage()

PSCFileSchema = BaseSchema.copy() + Schema((

    TextField('title',
        default='',
        searchable=1,
        accessor="Title",
        widget=StringWidget(
            label="File Description",
            label_msgid="label_file_title",
            description="File description. Normally something like "
                        "'Product Package', 'Windows Installer',  - "
                        "or 'Events subsystem' if you have several "
                        "separate modules. The actual file name will "
                        "be the same as the file you upload.",
            description_msgid="help_file_title",
            i18n_domain="plonesoftwarecenter",
        ),
    ),

    FileField('downloadableFile',
        primary=1,
        required=1,
        widget=FileWidget(
            label="File",
            label_msgid="label_file_description",
            description="Click 'Browse' to upload a release file.",
            description_msgid="help_file_description",
            i18n_domain="plonesoftwarecenter",
        ),
        storage=downloadableFileStorage,
    ),

    StringField('platform',
        required=1,
        searchable=0,
        vocabulary='getPlatformVocab',
        widget=SelectionWidget(
            label="Platform",
            label_msgid="label_file_platform",
            description="",
            description_msgid="help_file_platform",
            i18n_domain="plonesoftwarecenter",
        ),
    ),

),

marshall = PrimaryFieldMarshaller(),

)
PSCFileSchema['id'].widget.visible = {'edit': 'hidden'}

class PSCFile(ATCTFileContent):
    """Contains the downloadable file for the Release."""

    implements(IFileContent)

    archetype_name = 'Downloadable File'
    immediate_view = default_view = 'psc_file_view'
    suppl_views = ()
    content_icon = 'file_icon.gif'
    schema = PSCFileSchema
    global_allow = False

    security = ClassSecurityInfo()

    # XXX: This should go away once ATCT is fixed to not mangle filenames
    def _cleanupFilename(self, filename, encoding=None, **kw):
        """Cleans the filename from unwanted or evil chars
        """
        # Do nothing for now, ATCT is too liberal with this.
        return filename

    security.declareProtected(permissions.View, 'getPlatformVocab')
    def getPlatformVocab(self):
        """Get the platforms available for selection via acquisition from
        the top-level projects container.
        """
        return DisplayList([(item, item) for item in \
                            self.getAvailablePlatforms()])

    security.declareProtected(permissions.ModifyPortalContent, 'setDownloadableFile')
    def setDownloadableFile(self, value, **kwargs):
        """Set id to uploaded id
        """
        self._setATCTFileContent(value, **kwargs)

registerType(PSCFile, config.PROJECTNAME)
