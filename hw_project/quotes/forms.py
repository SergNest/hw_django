from django.forms import ModelForm, CharField, TextInput
from .models import Quote, Autor


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']