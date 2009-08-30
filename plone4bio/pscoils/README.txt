plone4bio.pscoils
===================

Overview
--------

The *plone4bio* package provides the possibility to add a new content
type, called `sequence', than can be either written by hand or imported
from a FASTA file, and to apply to that sequence a program, called
`predictor', that gives a back a plot of predicted probabilites for the
sequence to have a given property (the property that the predictor tries
to determine). 

A predictor can try to assess if a protein sequence is trans-membrane,
whether a signal peptide exists, and so on. 

The *plone4bio.pscoils* is a package that defines a simple prediction 
object based on predictor *biocomp.pscoils* 
(see http://plone4bio.org/svn/biocomp.pscoils/trunk/doc/ for more information).

Creating a sequence
-------------------

Let us create some sequences.

    >>> from Products.PloneTestCase import ptc
    >>> self.login()
    >>> self.setRoles(('Manager',))
    >>> self.portal.invokeFactory('SeqRecord', u'ferritin', title=u'Ferritin')
    'ferritin'
    >>> ferritin = getattr(self.portal, u'ferritin')

The Sequence objects are simple Zope 3-like persistent content items, so we
will configure the project using theirs properties.

    >>> ferritin.descritpion = u"Ferritin sequence"
    >>> ferritin.sequence = u"CMSPDQWDKEAAQYDAHAQEFEKKSHRNNGTPEADQYRHMASQYQAMAQKLKAIANQLKKGSETCR"
    >>> ferritin.alphabet="Bio.Alphabet.ProteinAlphabet"

Now we can run the pscoils predictor over the sequence:

    >>> from Products.CMFCore.utils import getToolByName
    >>> pred_tool = getToolByName(self.portal, 'plone4bio_predictors')
    >>> pred_tool('pscoils', ferritin, store=True)
    <SeqRecord at /plone/ferritin>
    >>> len(ferritin.features) == len(ferritin.sequence)
    True
    >>> ferritin.features[0].id
    '<unknown id>'
    >>> str(ferritin.features[0].location)
    '[0:0]'
    >>> ferritin.features[0].location_operator
    ''
    >>> ferritin.features[0].qualifiers
    {'gg': 0.926..., 'hept_seq': 'a', 'gcc': 1.323...e-06, 'score': 0.480..., 'prob': 5.713...e-08}
    >>> ferritin.features[0].ref
    >>> ferritin.features[0].ref_db
    >>> ferritin.features[0].strand
    >>> ferritin.features[0].sub_features
    []
    >>> ferritin.features[0].type
    'pscoils'
	
Developer Notes
---------------

The plone4bio* plone products are mainly developed on Debian Stable, so
they are mainly tested in that environment. Usually there should be no
problem in installing the products in other Zope/Plone environments.

Maintainer
----------

Mauro Amico (mauro AT biodec DOT com) is the active maintainer of the
*plone4bio* framework.
