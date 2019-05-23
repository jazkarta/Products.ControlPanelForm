import sys
import plone.app.controlpanel
import form
import widgets


sys.modules['plone.app.controlpanel.form'] = form
sys.modules['plone.app.controlpanel.widgets'] = widgets
