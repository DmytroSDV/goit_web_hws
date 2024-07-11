from django import forms
from .models import Author, Quote, Tag
from .widgets import TagCheckboxSelectMultiple

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=TagCheckboxSelectMultiple)
    
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']

class SearchForm(forms.Form):
    search_tags = forms.CharField(label='Search tags', max_length=50)