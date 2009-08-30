from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
from Products.CMFCore.utils import getToolByName
import plone4bio.base
import plone4bio.pscoils


@onsetup
def setup_product():
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', plone4bio.base)
    zcml.load_config('configure.zcml', plone4bio.pscoils)
    fiveconfigure.debug_mode = False
    ztc.installPackage('plone4bio.base')
    ztc.installPackage('plone4bio.pscoils')

class BaseTestCase(ptc.PloneTestCase):
    """Base test case for.
    """

    def afterSetUp(self):
        qi = getToolByName(self.portal, 'portal_quickinstaller')
        products = ['plone4bio.base', 'plone4bio.pscoils']
        for product in products:
            if not qi.isProductInstalled(product):
                qi.installProduct(product)

setup_product()
ptc.setupPloneSite(products=['plone4bio'])
