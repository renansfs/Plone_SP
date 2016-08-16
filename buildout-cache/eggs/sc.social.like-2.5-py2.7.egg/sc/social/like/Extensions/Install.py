# -*- coding: utf-8 -*-
from sc.social.like.config import PROJECTNAME
from plone import api


def uninstall(portal, reinstall=False):
    if not reinstall:
        profile = 'profile-%s:uninstall' % PROJECTNAME
        setup_tool = api.portal.get_tool(name='portal_setup')
        setup_tool.runAllImportStepsFromProfile(profile)
        return 'Ran all uninstall steps.'
