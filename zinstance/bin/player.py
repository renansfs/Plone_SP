#!/home/vagrant/venv/bin/python
#
# The Python Imaging Library
# $Id$
#

from __future__ import print_function

try:
    from tkinter import *
except ImportError:
    from Tkinter import *



import sys
sys.path[0:0] = [
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Plone-4.3.10-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Pillow-3.2.0-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.contenttypes-1.1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.cover-1.2b1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFPlone-4.3.10rc1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PloneSoftwareCenter-1.6.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.watcherlist-2.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/auslfe.formonline.content-0.8.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone4.csrffixes-1.0.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PloneFormGen-1.7.19-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/auslfe.formonline.pfgadapter-0.7.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/sc.photogallery-1.0b1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.Ploneboard-3.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.portlet.embed-1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.fingerpointing-1.1b1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.lazysizes-1.5.0b1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/sc.social.like-2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.GenericSetup-1.8.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.siterss-0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.Poi-2.2.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/webcouturier.dropdownmenu-2.3.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.portlet.calendar-0.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/setuptools-23.1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.browserlayer-2.1.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.DataGridField-1.9.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.AddRemoveWidget-1.5.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.formlib-4.3.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Zope2-2.13.24-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.schema-4.2.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.interface-3.6.7-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.component-3.9.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFQuickInstallerTool-3.0.13-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFDefault-2.2.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFCore-2.2.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.Archetypes-1.9.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.supermodel-1.2.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.registry-1.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.memoize-1.1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.upgrade-1.3.25-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.registry-1.2.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.layout-2.3.14-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.api-1.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Acquisition-2.13.9-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.transformchain-1.2.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.directives.form-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.imaging-1.0.13-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/lxml-2.3.6-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.globalrequest-1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PlonePAS-5.0.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.form-3.2.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/AccessControl-3.0.11-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/python_dateutil-1.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFPlacefulWorkflow-1.5.13-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.i18n-2.0.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.portlets-2.2.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.portlets-2.5.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.controlpanel-2.3.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.SimpleAttachment-5.0.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.dexterity-2.2.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.textfield-1.2.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.relationfield-1.2.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.dexterity-2.0.18-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.js.cycle2-1.0b2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.js.jqueryui-1.8.16.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.jquerytools-1.5.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PythonField-1.1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.TemplateFields-1.2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.TALESField-1.1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/cssselect-0.9.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.monkeypatcher-1.1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.locking-2.0.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.protect-3.0.16-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.contentratings-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/cioppino.twothumbs-2.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ArchAddOn-1.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.container-3.11.2-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/transaction-1.1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plonetheme.sunburst-1.4.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plonetheme.classic-1.3.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.theme-2.1.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.session-3.5.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.portlet.static-2.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.portlet.collection-2.1.10-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.intelligenttext-2.1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.fieldsets-2.0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.contentrules-2.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.batching-1.0.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.workflow-2.1.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.vocabularies-2.1.24-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.viewletmanager-2.0.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.uuid-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.users-1.2.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.search-1.1.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.redirector-1.2.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.locales-4.3.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.linkintegrity-1.5.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.jquery-1.7.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.i18n-2.0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.form-2.2.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.folder-1.1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.discussion-2.2.18-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.customerize-1.2.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.contentrules-3.0.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.contentmenu-2.0.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.contentlisting-1.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.content-2.1.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.collection-1.0.13-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.blob-1.5.17-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.customerize-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/borg.localrole-3.0.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/archetypes.referencebrowserwidget-2.5.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/archetypes.querywidget-1.1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/ZODB3-3.10.5-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.statusmessages-4.1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.TinyMCE-1.3.21-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ResourceRegistries-2.2.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PortalTransforms-2.1.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PloneLanguageTool-3.2.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PlacelessTranslationService-2.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PasswordResetTool-2.0.19-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.MimetypesRegistry-2.0.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ExternalEditor-1.1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ExtendedPathIndex-3.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFFormController-3.0.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFEditions-2.2.20-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFDynamicViewFTI-4.1.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFDiffTool-2.2.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFCalendar-2.2.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.CMFActionIcons-2.1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ATContentTypes-2.1.19-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/ExtensionClass-2.13.2-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/DateTime-3.0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.uuid-1.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.tiles-1.5.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.scale-1.4.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.namedfile-3.0.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.behavior-1.1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.autoform-1.6.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.tiles-1.0.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.lockingbehavior-1.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.iterate-2.1.17-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.blocks-2.2.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Missing-2.13.1-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.grok-1.3.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.z3cform.datetimewidget-1.2.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.js.galleria-1.2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.js.bootstrap-2.3.1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/pytz-2013b-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.versioningbehavior-1.2.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.querystring-1.1.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.querystring-1.2.10-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.event-1.1.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/wicked-1.1.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.theming-1.1.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.openid-2.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.caching-1.1.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.security-3.7.4-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.browser-1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.BTreeFolder2-2.13.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.proxy-3.6.1-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zLOG-2.11.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/initgroups-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/docutils-0.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/ZConfig-2.9.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Record-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ZCatalog-2.13.27-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Persistence-2.13.2-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/MultiMapping-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/DocumentTemplate-2.13.2-py2.7-linux-i686.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.formlib-1.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.folder-1.0.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.validation-2.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.Marshall-2.1.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.contentmigration-2.1.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.z3cform-0.7.7-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/decorator-3.4.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/future-0.13.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.rfc822-1.1.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/six-1.10.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Unidecode-0.04.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/feedparser-5.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/archetypes.schemaextender-2.1.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.alterego-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.contenttree-1.0.14-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.relationfield-0.6.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.intid-1.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/five.intid-1.0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.directives.dexterity-1.0.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.schemaeditor-1.3.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.namedfile-1.0.15-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.form-4.0.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.component-3.9.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/rwproperty-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/contentratings-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zc.buildout-2.5.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.stringinterp-1.0.13-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.content-3.5.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.caching-1.0.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.outputfilters-1.15.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Markdown-2.0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/python_gettext-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.ATReferenceBrowserWidget-3.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.publisher-3.10.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.file-3.6.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.app.drafts-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.subrequest-1.7.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.resource-1.0.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/diazo-1.1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.viewlet-1.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.view-2.8-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.site-1.6.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.security-1.6.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.component-2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/grokcore.annotation-1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/martian-0.14-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.container-3.9.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.recurrence-1.2.6-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.datetime-1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.event-1.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/icalendar-3.10-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/collective.elephantvocabulary-0.2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.resourceeditor-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/roman-1.4.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.openid-2.0.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.cachepurging-1.0.11-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/plone.formwidget.autocomplete-1.2.9-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zc.relation-1.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/z3c.objpath-1.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.intid-3.7.1-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.keyreference-3.6.4-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.app.pagetemplate-3.11.2-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.dublincore-3.7.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/experimental.cssselect-0.3-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.copypastemove-3.7.0-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/vagrant/Plone_SP/buildout-cache/eggs/zope.hookable-3.4.1-py2.7-linux-i686.egg',
  ]


from PIL import Image, ImageTk
import sys


# --------------------------------------------------------------------
# an image animation player

class UI(Label):

    def __init__(self, master, im):
        if isinstance(im, list):
            # list of images
            self.im = im[1:]
            im = self.im[0]
        else:
            # sequence
            self.im = im

        if im.mode == "1":
            self.image = ImageTk.BitmapImage(im, foreground="white")
        else:
            self.image = ImageTk.PhotoImage(im)

        Label.__init__(self, master, image=self.image, bg="black", bd=0)

        self.update()

        try:
            duration = im.info["duration"]
        except KeyError:
            duration = 100
        self.after(duration, self.next)

    def next(self):

        if isinstance(self.im, list):

            try:
                im = self.im[0]
                del self.im[0]
                self.image.paste(im)
            except IndexError:
                return  # end of list

        else:

            try:
                im = self.im
                im.seek(im.tell() + 1)
                self.image.paste(im)
            except EOFError:
                return  # end of file

        try:
            duration = im.info["duration"]
        except KeyError:
            duration = 100
        self.after(duration, self.next)

        self.update_idletasks()


# --------------------------------------------------------------------
# script interface

if __name__ == "__main__":

    if not sys.argv[1:]:
        print("Syntax: python player.py imagefile(s)")
        sys.exit(1)

    filename = sys.argv[1]

    root = Tk()
    root.title(filename)

    if len(sys.argv) > 2:
        # list of images
        print("loading...")
        im = []
        for filename in sys.argv[1:]:
            im.append(Image.open(filename))
    else:
        # sequence
        im = Image.open(filename)

    UI(root, im).pack()

    root.mainloop()
