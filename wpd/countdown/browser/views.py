from zope.interface import Interface
from zope.component import adapts
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.schema import Date, URI

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from Acquisition import aq_inner, aq_parent

from plone.app.registry.browser import controlpanel

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase

from Products.CMFPlone.interfaces import IPloneSiteRoot

class IWPDSchema(Interface):

    wpd_date    = Date(title=_(u'Date of the World Plone Day'),
                       required=True)

    wpd_url     = URI(title=_(u'URL to a local WPD Website'),
                       required=False)

class WPDSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IWPDSchema
    label = _(u"World Plone Day settings")
    description = _(u"""""")

    def updateFields(self):
        super(WPDSettingsEditForm, self).updateFields()
    
    def updateWidgets(self):
        super(WPDSettingsEditForm, self).updateWidgets()

class WPDSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = WPDSettingsEditForm
