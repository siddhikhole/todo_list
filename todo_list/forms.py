from django import forms
from .models import List


class listform(forms.ModelForm):
	class Meta(object):
		model=List
		fields=["item","completed"]