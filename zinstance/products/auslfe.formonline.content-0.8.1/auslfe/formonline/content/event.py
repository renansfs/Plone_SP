# -*- coding: utf-8 -*-

from zope.annotation import IAnnotations
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_base, aq_parent
from auslfe.formonline.content import formonline_contentMessageFactory as _
from auslfe.formonline.content import logger
try:
    from Products.PageTemplates.GlobalTranslationService import getGlobalTranslationService
    PLONE3 = True
except ImportError:
    from zope.i18n import translate as i18ntranslate
    PLONE3 = False
from email.MIMEText import MIMEText
from Products.CMFPlone.utils import safe_unicode
import socket
from Products.CMFPlone.utils import log_exc, log
from email.Utils import parseaddr, formataddr
from email.MIMEMultipart import MIMEMultipart
from reStructuredText import HTML as rstHTML

def formOnlineNotificationMail(formonline, event):
    """
    When the state of a Form Online change send a notification email.
    """
    addresses = []
    ann = IAnnotations(formonline)
    
    if event.action == 'submit':
        ann = IAnnotations(formonline)
        # See auslfe.formonline.tokenaccess
        if ann.get('share-tokens'):
            addresses = (ann['share-tokens']['email'],)
        else:
            addresses = getAddressesFromRole('Editor', formonline)
    elif event.action == 'approval':
        addresses = getAddressesFromRole('Reviewer', formonline)
    elif event.action == 'dispatch' or event.action == 'retract_approval' or event.action == 'retract_dispatch':
        addresses = getAddressesFromRole('Owner', formonline)
        if ann.get('owner-email'):
            addresses.append(ann.get('owner-email'))

    if addresses:
        sendNotificationMail(formonline, event.action, addresses)

def get_inherited(formonline):
    """Return True if local roles are inherited here.
    """
    if getattr(aq_base(formonline), '__ac_local_roles_block__', None):
        return False
    return True

def get_global_roles(formonline):
    """Returns a tuple with the acquired local roles."""
    formonline = aq_inner(formonline)
    
    if not get_inherited(formonline):
        return []
    
    portal = getToolByName(formonline, 'portal_url').getPortalObject()
    result = []
    
    local_roles = formonline.acl_users._getLocalRolesForDisplay(formonline)
    for user, roles, role_type, name in local_roles:
        result.append([user, list(roles), role_type, name])
    
    cont = True
    if portal != formonline:
        parent = aq_parent(formonline)
        while cont:
            if not getattr(parent, 'acl_users', False):
                break
            userroles = parent.acl_users._getLocalRolesForDisplay(parent)
            for user, roles, role_type, name in userroles:
                # Find user in result
                found = 0
                for user2, roles2, type2, name2 in result:
                    if user2 == user:
                        # Check which roles must be added to roles2
                        for role in roles:
                            if not role in roles2:
                                roles2.append(role)
                        found = 1
                        break
                if found == 0:
                    # Add it to result and make sure roles is a list so
                    # we may append and not overwrite the loop variable
                    result.append([user, list(roles), role_type, name])
            if parent == portal:
                cont = False
            elif not get_inherited(parent):
                # Role acquired check here
                cont = False
            else:
                parent = aq_parent(parent)

    # Tuplize all inner roles
    for pos in range(len(result)-1,-1,-1):
        result[pos][1] = tuple(result[pos][1])
        result[pos] = tuple(result[pos])

    return tuple(result)

def getAddressesFromRole(role, formonline):
    """
    Returns a list of email of users with a specific role on a Form Online content,
    from a local roles structure."""
    pm = getToolByName(formonline,'portal_membership')
    globals_roles = get_global_roles(formonline)
    users = []
    for user,roles,role_type,name in globals_roles:
        if role in roles:
            member = pm.getMemberById(user)
            if member:
                users.append(member.getProperty('email'))
    return users

def sendNotificationMail(formonline, worfklow_action, addresses):
    """
    Send a notification email to the list of addresses
    """
    portal_url = getToolByName(formonline, 'portal_url')
    portal = portal_url.getPortalObject()
    portal_membership = getToolByName(portal, 'portal_membership')
    portal_workflow = getToolByName(portal, 'portal_workflow')
    portal_catalog = getToolByName(portal, 'portal_catalog')
    
    plone_utils = getToolByName(portal, 'plone_utils')
    charset = plone_utils.getSiteEncoding()

    def su(value):
        return safe_unicode(value, encoding=charset)
    
    formonlineCreator = formonline.Creator()
    formonlineCreatorInfo = portal_membership.getMemberInfo(formonlineCreator)
    formonlineAuthor = formonlineCreator
    if formonlineCreatorInfo:
        formonlineAuthor = formonlineCreatorInfo['fullname'] or formonlineCreator

    insertion_date = formonline.toLocalizedTime(formonline.created())

    if PLONE3:
        _ = getGlobalTranslationService().translate
    else:
        _ = i18ntranslate

    ann = IAnnotations(formonline)
    # See auslfe.formonline.tokenaccess
    if ann.get('share-tokens') and worfklow_action == 'submit':
        path = '/'.join(formonline.getPhysicalPath()).replace('/%s/' % portal.getId(), '')
        formonline_url = '%s/@@consume-powertoken-first?path=%s&token=%s' % (
                                                                             portal_url(),
                                                                             path,
                                                                             ann['share-tokens']['view']
                                                                             )
        logger.debug(formonline_url)
    else:
        formonline_url = su(formonline.absolute_url())

    comment = portal_workflow.getInfoFor(formonline, 'comments')
    if not comment:
        try:
            comment = _(msgid='comment_retract',
                        default=u'No comments',
                        domain="auslfe.formonline.content",
                        context=formonline)
        except TypeError:
            # On Plone 4
            comment = _(msgid='comment_retract',
                        default=u'No comments',
                        domain="auslfe.formonline.content",
                        context=formonline.REQUEST)
        
    lines = comment.splitlines()
    comment = ""
    for l in lines:
        comment+="\t%s\n" % l

    mapping = dict(formonline_title = su(formonline.title_or_id()),
                   insertion_date = su(insertion_date),
                   formonline_owner = su(formonlineAuthor),
                   formonline_url = formonline_url,
                   comment = comment,
                   )
    
    formOnlineAdapter_UID = ann.get('formOnlineAdapter','')
    formOnlineAdapter = formOnlineAdapter_UID and portal_catalog.unrestrictedSearchResults(UID=formOnlineAdapter_UID) or []
    
    # get subject and text of email from the fields of FormOnlineAdapter
    if formOnlineAdapter:
        form_online_adapter = formOnlineAdapter[0]._unrestrictedGetObject()
        if worfklow_action == 'submit':
            subject = form_online_adapter.getFormOnlineSubmitSubject()
            text = form_online_adapter.getFormOnlineSubmitMessage()
        elif worfklow_action == 'approval':
            subject = form_online_adapter.getFormOnlineApprovalSubject()
            text = form_online_adapter.getFormOnlineApprovalMessage()
        elif worfklow_action == 'dispatch':
            subject = form_online_adapter.getFormOnlineDispatchSubject()
            text = form_online_adapter.getFormOnlineDispatchMessage()
        elif worfklow_action == 'retract_approval' or worfklow_action == 'retract_dispatch':
            subject = form_online_adapter.getFormOnlineRetractSubject()
            text = form_online_adapter.getFormOnlineRetractMessage()
        text = text.decode("utf-8")
        for variable in mapping:
            text = text.replace("${%s}" % variable, mapping[variable])
    else:
        # Let's keep ol hardcoded messages, so FormOnline contents created before this version will still works
        if worfklow_action == 'submit':
            subject = _(msgid='subject_pending_approval',
                        default=u'[Form Online] - Form Online in pending state approval',
                        domain="auslfe.formonline.content",
                        context=formonline)
            text = _(msgid='mail_text_approval_required', default=u"""Dear user,
    
this is a personal communication regarding the Form Online **${formonline_title}**, created on **${insertion_date}** by **${formonline_owner}**.

It is waiting for your approval. Follow the link below for perform your actions:

${formonline_url}

Regards
""", domain="auslfe.formonline.content", context=formonline, mapping=mapping)
    
        elif worfklow_action == 'approval':
            subject = _(msgid='subject_pending_dispatch',
                        default=u'[Form Online] - Form Online in pending state dispatch',
                        domain="auslfe.formonline.content",
                        context=formonline)
            text = _(msgid='mail_text_dispatch_required', default=u"""Dear user,
    
this is a personal communication regarding the Form Online **${formonline_title}**, created on **${insertion_date}** by **${formonline_owner}**.

The request has been approved and it's waiting for your confirmation. Follow the link below for perform your actions:

${formonline_url}

Regards
""", domain="auslfe.formonline.content", context=formonline, mapping=mapping)
    
        elif worfklow_action == 'dispatch':
            subject = _(msgid='subject_dispatched',
                        default=u'[Form Online] - Form Online approved',
                        domain="auslfe.formonline.content",
                        context=formonline)
            text = _(msgid='mail_text_dispatched', default=u"""Dear user,
    
this is a personal communication regarding the Form Online **${formonline_title}**.

The request has been *approved*. Follow the link below to see the document:

${formonline_url}

Regards
""", domain="auslfe.formonline.content", context=formonline, mapping=mapping)
    
        elif worfklow_action == 'retract_approval' or worfklow_action == 'retract_dispatch':
            subject = _(msgid='subject_rejected',
                        default=u'[Form Online] - Form Online rejected',
                        domain="auslfe.formonline.content",
                        context=formonline)
            text = _(msgid='mail_text_rejected', default=u"""Dear user,
    
this is a personal communication regarding the Form Online **${formonline_title}**.

The request has been *rejected*. The overseer provided the following comment::

${comment}

Follow the link below to see the document:

${formonline_url}

Regards
""", domain="auslfe.formonline.content", context=formonline, mapping=mapping)
        # converte il testo in HTML perchè sendEmail si aspetta che arrivi un messaggio HTML,
        # come nel caso default in cui l'annotazione del formOnlineAdapter è presente sul Form
        text = rstHTML(text,input_encoding='utf-8',output_encoding='utf-8').decode("utf-8")
    
    sendEmail(formonline, addresses, subject, text)


def sendEmail(formonline, addresses, subject, rstText, cc = None):
    """
    Send a email to the list of addresses
    """    
    portal_url  = getToolByName(formonline, 'portal_url')
    plone_utils = getToolByName(formonline, 'plone_utils')
    transforms = getToolByName(formonline, 'portal_transforms')

    portal      = portal_url.getPortalObject()
    mailHost    = plone_utils.getMailHost()
    charset     = portal.getProperty('email_charset', '')
    if not charset:
        charset = plone_utils.getSiteEncoding()
    from_address = portal.getProperty('email_from_address', '')

    if not from_address:
        log('Cannot send notification email: email sender address not set')
        return
    from_name = portal.getProperty('email_from_name', '')
    mfrom = formataddr((from_name, from_address))
    if parseaddr(mfrom)[1] != from_address:
        # formataddr probably got confused by special characters.
        mfrom - from_address

    email_msg = MIMEMultipart('alternative')
    email_msg.epilogue = ''

    # Translate the body text
    if PLONE3:
        translate = getGlobalTranslationService().translate
    else:
        translate = i18ntranslate

    # We must choose the body charset manually
    for body_charset in (charset, 'UTF-8', 'US-ASCII'):
        try:
            rstText = rstText.encode(body_charset)
        except UnicodeError:
            pass
        else:
            break

    # Text came from HTML text fields inside adapter, so I will convert it to simple text 
    stream = transforms.convertTo('text/plain', rstText, mimetype='text/html')
    textPart = MIMEText(stream.getData().strip(), 'plain', body_charset)
    email_msg.attach(textPart)
    htmlPart = MIMEText(renderHTML(rstText, charset=body_charset),
                        'html', body_charset)
    email_msg.attach(htmlPart)

    subject = safe_unicode(subject, charset)

    for address in addresses:
        address = safe_unicode(address, charset)
        if address:
            try:
                # Note that charset is only used for the headers, not
                # for the body text as that is a Message already.
                mailHost.secureSend(message = email_msg,
                                    mto = address,
                                    mfrom = mfrom,
                                    subject = subject,
                                    charset = charset)
            except socket.error, exc:
                log_exc(('Could not send email from %s to %s regarding issue '
                         'in content %s\ntext is:\n%s\n') % (
                        mfrom, address, formonline.absolute_url(), email_msg))
                log_exc("Reason: %s: %r" % (exc.__class__.__name__, str(exc)))
            except:
                raise

def renderHTML(rstText, lang='en', charset='utf-8'):
    """Convert the given rST into a full XHTML transitional document.
    """

    kwargs = {'lang': lang,
              'charset': charset,
              'body': rstText}
    
    return htmlTemplate % kwargs

htmlTemplate = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xml:lang="%(lang)s"
      lang="%(lang)s">

  <head>
     <meta http-equiv="Content-Type" content="text/html; charset=%(charset)s" />

    <style type="text/css" media="all">
<!--
body {
    font-size: 0.9em;
}

h4 {
    font-size: 1.2em;
    font-weight: bold;
}

dt {
    font-weight: bold;
}
-->
    </style>

  </head>

  <body>
%(body)s
  </body>
</html>
"""
