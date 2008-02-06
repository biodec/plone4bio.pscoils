from zope.interface import Interface, Invalid, invariant, implements
from zope.component.interfaces import IObjectEvent

from zope import schema
from zope.app.container.constraints import containers, contains

from plone.app.vocabularies.users import UsersSource

from plone4bio.base import Plone4BioMessageFactory as _
from plone4bio.base.interfaces import IGenericPrediction

class IPscoilsPrediction(IGenericPrediction):
    """ """
