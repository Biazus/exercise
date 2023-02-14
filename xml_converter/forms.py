from django import forms


class ConverterForm(forms.Form):
    file = forms.FileField(label='XML File')
