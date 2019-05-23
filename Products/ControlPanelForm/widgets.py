
from zope.formlib.itemswidgets import MultiSelectWidget
from zope.formlib.itemswidgets import DropdownWidget
from zope.formlib.widget import renderElement
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.schema.interfaces import ITitledTokenizedTerm
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFPlone import PloneMessageFactory as _
from plone.app.form.widgets import MultiCheckBoxWidget

WEEKDAYS = (('Monday', 0),
            ('Tuesday', 1),
            ('Wednesday', 2),
            ('Thursday', 3),
            ('Friday', 4),
            ('Saturday', 5),
            ('Sunday', 6))


class DropdownChoiceWidget(DropdownWidget):
    """ """

    def __init__(self, field, request):
        """Initialize the widget."""
        super(DropdownChoiceWidget, self).__init__(field,
            field.vocabulary, request)


class MultiCheckBoxVocabularyWidget(MultiCheckBoxWidget):
    """ """

    def __init__(self, field, request):
        """Initialize the widget."""
        super(MultiCheckBoxVocabularyWidget, self).__init__(field,
              field.value_type.vocabulary, request)
