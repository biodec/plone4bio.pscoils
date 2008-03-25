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
(see http://www.plone4bio.org/svn/biocomp.pscoils/README for more information).

Creating a sequence
-------------------

Let us create some sequences.

	>>> self.portal.invokeFactory('Sequence','ferritin')
	'ferritin'
	>>> ferritin = getattr(self.portal,'ferritin')

The Sequence objects are simple Zope 3-like persistent content items, so we 
will configure the project using theirs properties.

	>>> ferritin.title = u"Ferritin"
	>>> ferritin.descritpion = u"Ferritin sequence"
	>>> ferritin.sequence = u"CMSPDQWDKEAAQYDAHAQEFEKKSHRNNGTPEADQYRHMASQYQAMAQKLKAIANQLKKGSETCR"
	
Now we can create a prediction over the sequence:

	>>> ferritin.invokeFactory('Pscoils Prediction','pscoils')
	'pscoils'
	>>> pscoils = getattr(ferritin,'pscoils')
	>>> pscoils.run()
	
	>>> pscoils.getState()
	'done'
	>>> (pscoils.result['index'] == range(0,len(ferritin.sequence)))
	True
	>>> (u''.join(pscoils.result['alpha']) == ferritin.sequence)
	True
	
Developer Notes
---------------

The plone4bio* plone products are mainly developed on Debian Stable, so
they are mainly tested in that environment. Usually there should be no
problem in installing the products in other Zope/Plone environments.

Maintainer
----------

Mauro Amico (amico AT biodec DOT com) is the active maintainer of the
*plone4bio.base* framework.
