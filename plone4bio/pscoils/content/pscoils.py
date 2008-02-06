__author__ = '''Mauro <mauro@biodec.com>'''
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import adapts
from zope.component.factory import Factory

from plone.memoize.instance import memoize

from plone4bio.base import Plone4BioMessageFactory as _
from plone4bio.base.content.generic import GenericPrediction
from plone4bio.pscoils.interfaces import IPscoilsPrediction

from OFS.OrderSupport import OrderSupport

import biocomp.pscoils

class Pscoils(GenericPrediction):
    implements(IPscoilsPrediction)
    portal_type = "Pscoils Prediction"
    predname = "pscoils"
    result = []
    
    # @memoize
    def xrange(self):
        return map(lambda r: r['index'], self.result)
    
    # @memoize
    def prob(self,index=None):
        if (index is None):
            return map(lambda r: r['prob'], self.result)
        else:
            return self.result[index]['prob']

    # @memoize
    def pred(self,index=None):
        if (index is None):
            return map(lambda r: r['pred'], self.result)
        else:
            return self.result[index]['pred']
    
    def do_prediction(self):
        sequence = self.getSequenceRaw()
        weight='un'
        wlambda=0.5
        win=21
        modeprofile=False
        modefasta=True
        labels='F'
        params=biocomp.pscoils.Params.Params(weight,win)
        # output = StringIO.StringIO()
        gg,gcc,prob,hept,score=biocomp.pscoils.pred_coil(sequence,len(sequence),params,biocomp.pscoils.seqScore)    
        self.result = map(lambda i: {'index':i, 
                                     'alpha':sequence[i], 
                                     'prob':prob[i],
                                     'hept':hept[i], 
                                     'score':score[i], 
                                     'gg':gg[i], 
                                     'gcc':gcc[i], 
                                     'pred':(prob[i]>0.5) and 'C' or 'L'}, range(0,len(sequence)))

    def getDataCharts(self):
        # import pdb; pdb.set_trace()
        regions = {}
        regions['chart'] = 'bar'
        regions['color'] = {'L':0xFF0000, 'C':0x00FFFF}
        regions['data'] = zip(self.xrange(),self.pred())
        return [regions,]
    
pscoilsFactory = Factory(Pscoils, title=_(u"Create a new pscoils prediction"))