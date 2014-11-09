from django import forms

class PostBank(forms.Form):
	sku = forms.CharField(max_length=24)
	name = forms.CharField(max_length=64)
    url = forms.ImageField(max_length=24)
