from django import forms

class InputCodePageForm(forms.Form):
    big_field = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control'}) , label='')
    