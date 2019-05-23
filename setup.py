from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='Products.ControlPanelForm',
      version=version,
      description="Plone 5 compatibility package for old Plone 4 packages",
      long_description=open(os.path.join("README.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone Control Panel',
      author='Jazkarta',
      author_email='info@jazkarta.com',
      url='http://jazkarta.com/',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.fieldsets',
          'plone.app.controlpanel',
          'plone.app.form',
          'plone.app.registry',
      ],
      )
