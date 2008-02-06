from zope.component import createObject
from zope.formlib import form

from plone.app.form import base
from plone.app.form.widgets.uberselectionwidget import UberMultiSelectionWidget

from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from plone4bio.pscoils.interfaces import IPscoilsPrediction
from plone4bio.base import Plone4BioMessageFactory as _

from plone.memoize.instance import memoize

pscoils_form_fields = form.Fields(IPscoilsPrediction)
#project_form_fields['managers'].custom_widget = UberMultiSelectionWidget
#project_form_fields['team'].custom_widget = UberMultiSelectionWidget

class PscoilsView(BrowserView):
    """Default view of a pscoils prediction.
    """    
    __call__ = ViewPageTemplateFile('pscoils/pscoils.pt') 
    
class PscoilsAddForm(base.AddForm):
    """Add form for prediction
    """    
    form_fields = pscoils_form_fields
    label = _(u"Add Pscoils Prediction")
    form_name = _(u"Edit Pscoils Prediction")
    def create(self, data):
        prediction = createObject(u"plone4bio.pscoils.Pscoils")
        form.applyChanges(prediction, self.form_fields, data)
        return prediction