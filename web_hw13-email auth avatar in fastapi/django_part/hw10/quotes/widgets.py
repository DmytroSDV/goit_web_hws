from django import forms
from .models import Tag

class TagCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, str):
            value = value.split(',')
        return super().render(name, value, attrs, renderer)

class TagSelectMultiple(forms.SelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, str):
            value = value.split(',')
        return super().render(name, value, attrs, renderer)

class TagSelectMultipleWidget(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if isinstance(value, str):
            value = value.split(',')
        return super().render(name, value, attrs, choices)