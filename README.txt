Plone packages with control panels from old plone.app.controlpanel versions
will cause a startup error when trying to import the control panel views.
This package fixes that. It will have to be added as a dependency on your
project.

As of February 2, 2019, known products with this problem include:

- Products.Maps
- collective.contentleadimage
- collective.quickupload
- collective.embedly
