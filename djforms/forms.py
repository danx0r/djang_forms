from django import forms

class DjangForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)

