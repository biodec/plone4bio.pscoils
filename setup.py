from setuptools import setup, find_packages
import sys, os

version = '1.0.0'

setup(name='plone4bio.pscoils',
      version=version,
      description="plone4bio: pscoils predictor",
      long_description=open(os.path.join("plone4bio", "pscoils", "README.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='bioinformatics',
      author='Mauro Amico',
      author_email='mauro@biodec.com',
      url='http://www.plone4bio.org/svn/plone4bio.pscoils',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone4bio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "setuptools",
          "plone4bio.base",
          "biocomp.pscoils",
      ],
      )
