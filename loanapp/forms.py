"""
from django.forms import ModelForm
from . models import approvals
"""
from django import forms
from crispy_forms.helper import FormHelper


"""
class MyForm(ModelForm):
	class Meta:
		model=approvals
		fields = '__all__'

"""

class ApprovalForm(forms.Form):


	
	Firstname          = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname','class': 'form-control'}))
	Lastname           = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname','class': 'form-control'}))
	Dependents         = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents','class': 'form-control'}))
	ApplicantIncome    = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income','class': 'form-control'}))
	CoapplicantIncome  = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income','class': 'form-control'}))
	LoanAmount         = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount','class': 'form-control'}))
	Loan_Amount_Term   = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan Term in Months','class': 'form-control'}))
	#Credit_History=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Last Credit Rating'}))
	Credit_History     = forms.ChoiceField(choices=[('0', 0),('1', 1),('2', 2),('3', 3)], widget=forms.Select(attrs={'class':'form-control'}))
	Gender             = forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')], widget=forms.Select(attrs={'class':'form-control'}))
	Married            = forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')], widget=forms.Select(attrs={'class':'form-control'}))
	Education          = forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not_Graduate', 'Not_Graduate')], widget=forms.Select(attrs={'class':'form-control'})) 
	Self_Employed      = forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')], widget=forms.Select(attrs={'class':'form-control'})) 
	Property_Area      = forms.ChoiceField(choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')], widget=forms.Select(attrs={'class':'form-control'}))

"""
	def __init__(self, *args, **kwargs):
	    super(ApprovalForm, self).__init__(*args, **kwargs)
	    self.helper = FormHelper()
	    self.helper.form_show_labels = False 

"""


