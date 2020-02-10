
from django import forms
from .models import  CassavaModel
from crispy_forms.helper import FormHelper



#class DogCatForm(forms.Form):
	#dogcatimage   = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname','class': 'form-control'}))
"""
	def __init__(self, *args, **kwargs):
	    super(DogCatForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_show_labels = False 
"""

class CassavaForm(forms.ModelForm):
	class Meta:
		model  = CassavaModel
		fields = ('name','imagefile')
