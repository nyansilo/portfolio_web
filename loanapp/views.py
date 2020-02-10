from django.contrib import messages
from django.shortcuts import render

from . forms import ApprovalForm
from . models import Approvals

import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter

""" ONE HOT ENCODED FUNCTION"""
def ohevalue(df):
	ohe_col       = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/ohe_column.pkl")
	cat_columns=['Gender','Married','Education','Self_Employed','Property_Area']
	df_processed = pd.get_dummies(df, columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	newdf=pd.DataFrame(newdict)
	return newdf	


"""APPROVE OR REJECT FUNCTION """
def approvereject(unit):
	try:
		mdl     = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/loan_model.pkl")
		scalers = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/scalers.pkl")
		X       = scalers.transform(unit)
		y_pred=mdl.predict(X)
		y_pred=(y_pred>0.58)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		K.clear_session()
		return (newdf.values[0][0],X[0])
	except ValueError as e:
		return (e.args[0])

"""LOAN FORM FUNCTION """
def loanform(request):
	if request.method=='POST':
		formdata=ApprovalForm(request.POST)
		if formdata.is_valid():
				Firstname = formdata.cleaned_data['Firstname']
				Lastname = formdata.cleaned_data['Lastname']
				Dependents = formdata.cleaned_data['Dependents']
				ApplicantIncome = formdata.cleaned_data['ApplicantIncome']
				CoapplicantIncome = formdata.cleaned_data['CoapplicantIncome']
				LoanAmount = formdata.cleaned_data['LoanAmount']
				Loan_Amount_Term = formdata.cleaned_data['Loan_Amount_Term']
				Credit_History = formdata.cleaned_data['Credit_History']
				Gender = formdata.cleaned_data['Gender']
				Married = formdata.cleaned_data['Married']
				Education = formdata.cleaned_data['Education']
				Self_Employed = formdata.cleaned_data['Self_Employed']
				Property_Area = formdata.cleaned_data['Property_Area']
				myDict = (request.POST).dict()
				print(myDict)
				df=pd.DataFrame(myDict, index=[0])
				print(df)
				Firstname=Firstname.capitalize()
				Lastname =Lastname.capitalize()
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				
				if int(df['LoanAmount'])<25000:
					messages.success(request,'Application Status for {} {}: {}'.format(Firstname,Lastname,answer))
				else:
					messages.success(request,'Invalid: Your Loan Request Exceeds $25,000 Limit')
	
	formdata=ApprovalForm()

	template = 'loan/loan_form.html'
	context = {'form_data' : formdata }
				
	return render(request, template, context )

"""
@api_view(["POST"])
def approvereject(request):
	try:
		mdl=joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		scalers=joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/scalers.pkl")
		X=scalers.transform(unit)
		y_pred=mdl .predict(X)
		y_pred=(y_pred>0.5)
		newdf=pd.DataFrame(y_pred, columns=['Status'])
		newdf=newdf.replace({True:'Approved', False:'Rejected'})
		return JsonResponse('Your Status is {}'.format(newdf), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)



def approvereject(request):
	try:
		mdl     = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanapp/loan_model.pkl")
		#mydata=pd.read_excel('/Users/sahityasehgal/Documents/Coding/bankloan/test.xlsx')
		mydata  = request.data
		unit    = np.array(list(mydata.values()))
		unit    = unit.reshape(1,-1)
		scalers = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/loanappscalers.pkl")
		X       = scalers.transform(unit)
		y_pred  = mdl.predict(X)
		y_pred  = (y_pred>0.58)
		newdf   = pd.DataFrame(y_pred, columns=['Status'])
		newdf   = newdf.replace({True:'Approved', False:'Rejected'})
		return ('Your Status is {}'.format(newdf))
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def loanform2(request):

	if request.method == 'POST':
		formdata = ApprovalForm(request.POST)
		if formdata.is_valid():
			Firstname         = formdata.cleaned_data['firstname']
			Lastname          = formdata.cleaned_data['lastname']
			Dependents        = formdata.cleaned_data['Dependents']
			ApplicantIncome   = formdata.cleaned_data['ApplicantIncome']
			CoapplicantIncome = formdata.cleaned_data['CoapplicantIncome']
			LoanAmount        = formdata.cleaned_data['LoanAmount']
			Loan_Amount_Term  = formdata.cleaned_data['Loan_Amount_Term']
			Credit_History    = formdata.cleaned_data['Credit_History']
			Gender            = formdata.cleaned_data['Gender']
			Married           = formdata.cleaned_data['Married']
			Education         = formdata.cleaned_data['Education']
			Self_Employed     = formdata.cleaned_data['Self_Employed']
			Property_Area     = formdata.cleaned_data['Property_Area']
			myDict = (request.POST).dict()
			df=pd.DataFrame(myDict, index=[0])
			answer=approvereject(ohevalue(df))[0]
			Xscalers=approvereject(ohevalue(df))[1]
			Firstname=Firstname.capitalize()
			Lastname =Lastname.capitalize()
			messages.success(request,'Application Status for {} {}: {}'.format(Firstname,Lastname,answer))

	formdata=ApprovalForm()

	template = 'loan/loan_form.html'
	context = {'form_data' : formdata }

				
	return render(request, template, context )



class ApprovalList(APIView):

	#List all puppies, or create a new puppy

	def get(self, request):
		approvals = Approvals.objects.all()
		serializer = ApprovalSerializer(approvals, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ApprovalSerializer(data=request.data)
		if serializer.is_valid():
			myData=serializer.data #this contain dictionary of key pair value ie key:value
			myDict = myData.values()
			print(myDict)
			df=pd.DataFrame(myDict)
			print(df)



			#serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApprovalsView(viewsets.ModelViewSet):
	queryset = Approvals.objects.all()
	serializer_class = ApprovalSerializer


"""
