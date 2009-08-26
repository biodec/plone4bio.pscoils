
from zope.interface import implements

from plone4bio.base.interfaces import IPredictor
from biocomp.pscoils import pred_coil
from biocomp.pscoils.Params import Params

class PSCoils:
    implements(IPredictor)

    def name(self):
        return "pscoils"

    def run(self, seqr, **kwargs):
        #TODO: manage kwargs
        weight='un'
        win=21
        params=Params(weight,win)
        return pred_coil(seqr, params)
