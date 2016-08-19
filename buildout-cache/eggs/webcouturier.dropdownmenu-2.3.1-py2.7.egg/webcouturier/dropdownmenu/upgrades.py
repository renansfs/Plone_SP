from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-webcouturier.dropdownmenu:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)


def upgrade_1000_to_1010(context):
    """If dropdownmenu_sunburst is after dropdownmenu in sunburst skin,
    reorder them"""
    skin = getToolByName(context, 'portal_skins')
    layers = skin.getSkinPath('Sunburst Theme').split(',')
    dds = layers.index('dropdownmenu_sunburst')
    dd = layers.index('dropdownmenu')
    if dds > dd:
        #switch them
        layers[dd] = 'dropdownmenu_sunburst'
        layers[dds] = 'dropdownmenu'
        path = ','.join(layers)
        skin.testSkinPath(path)
        sels = skin._getSelections()
        sels['Sunburst Theme'] = path
