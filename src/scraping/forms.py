from django import forms
from .models import City, Language


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                  to_field_name='slug',
                                  widget=forms.Select(attrs={'class' : 'form-control'}),
                                  label='Город'
                                  )
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                      to_field_name='slug',
                                      widget=forms.Select(attrs={'class' : 'form-control'}),
                                      label='Язык'
                                      )
