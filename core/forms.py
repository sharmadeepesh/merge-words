from django import forms

class wordForm(forms.Form):
	word = forms.CharField(widget= forms.Textarea)