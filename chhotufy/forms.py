from django import forms
class Form(forms.Form):
    url=forms.URLField()
