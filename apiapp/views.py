from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from PIL import Image


from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages

from apiapp import serializers
from . serializers import ProjectListlSerializer
from . serializers import ApprovalSerializer
from . serializers import CassavaSerializer
from . serializers import DogCatSerializer


from projectapp.models import Project

from loanapp.models import Approvals
from loanapp.views import ohevalue
from loanapp.views import approvereject

from cassavaapp.models import CassavaModel
from cassavaapp.views import cassavapredict

from dogcatapp.models import DogCatModel
from dogcatapp.views import dogorcat

from django.shortcuts import render
import base64
import pandas as pd




# Create your views here.

""" START PROJECTAPP API ENDPOINTS """
class ProjectListApiView(APIView):
	
	serializer_class = serializers.ProjectListlSerializer
	def get(self, request):
		try:
			projectlist = Project.objects.all()
			serializer = ProjectListlSerializer(projectlist,  context={'request': request},many=True)
			return Response(serializer.data)

		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

""" END PROJECTAPP API ENDPOINTS """


""" START CASSAVAAPP API ENDPOINTS """
class CassavaApiView(APIView):
	
	serializer_class = serializers.CassavaSerializer
	def get(self, request):
		try:
			cassavas = CassavaModel.objects.all()
			serializer = CassavaSerializer(cassavas,  context={'request': request},many=True)
			return Response(serializer.data)

		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

	def post(self,request):
		try:	
			serializer  = self.serializer_class(data=request.data)
			if serializer.is_valid():
				#serializer.save()
				#myData=serializer.data #This want take value which are in db
				name = request.data['name']
				imagefile = request.data['imagefile']
				#other way around
				#name = list(myData.values())[0]
				#imgfile = list(myData.values())[2]
				uploadedImg = imagefile
				name = name.capitalize()
				prediction = cassavapredict(uploadedImg)
				message = 'Hello {} your prediction is {}'.format(name,prediction)
				return Response({'message':message})
				#return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(
					serializer.errors,
					status = status.HTTP_400_BAD_REQUEST
				)	
		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)		

""" END CASSAVAAPP API ENDPOINTS """



""" START DOGCATAPP API ENDPOINTS """

class ImageUploadParser(FileUploadParser):
	media_type = 'image/*'

class DogCatApiView(APIView):



	parser_class = (ImageUploadParser,)
	
	serializer_class = serializers.DogCatSerializer
	def get(self, request, *args, **kwargs):
		try:
			dogcats = DogCatModel.objects.all()
			serializer = DogCatSerializer(dogcats,  context={'request': request},many=True)
			return Response(serializer.data)

		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

	def post(self,request):
		try:	
			serializer  = self.serializer_class(data=request.data,context={'request': request})
			if serializer.is_valid():
				#serializer.save()
				myData=serializer.data #This want take value which are in db
				name = request.data['name']
				imagefile = request.data['imagefile']

				#other way around
				#name = list(myData.values())[1]
				#imgfile = list(myData.values())[2]

				uploadedImg = imagefile
				name = name.capitalize()
				prediction = dogorcat(uploadedImg)
				message = 'Hello {} your prediction is {}'.format(name,prediction)
				#message = 'Hello {} your prediction is {}'.format(name,imagefile)
				return Response({'message':message})
				#return Response(serializer.data, status=status.HTTP_201_CREATED)
				#return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe='True')
			
			else:
				return Response(
					serializer.errors,
					status = status.HTTP_400_BAD_REQUEST
				)	
		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)		

""" END DOGCATAPP API ENDPOINTS """


""" START LOANAPP API ENDPOINTS """
class LoanApiView(APIView):
	
	serializer_class = serializers.ApprovalSerializer
	def get(self, request):
		approvals = Approvals.objects.all()
		serializer = ApprovalSerializer(approvals, many=True)
		return Response(serializer.data)


	def post(self,request):
		try:	
			serializer  = self.serializer_class(data=request.data)
			if serializer.is_valid():
				myData=serializer.data
				#this contain dictionary of key pair value ie key:value
				myDict = myData 
				#this will contain only value needed for the model
				df=pd.DataFrame(myDict, index=[0])
				answer=approvereject(ohevalue(df))[0]
				message = 'Your Status is {}'.format(answer)
				#message =  f'Your Status is {message}'
				#return JsonResponse('Your Status is {}'.format(myDict), safe=False)
				return Response({'message':message})
			
			else:
				return Response(
					serializer.errors,
					status = status.HTTP_400_BAD_REQUEST
				)	
		except ValueError as e:
			return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

""" END PROJECTS API ENDPOINTS """












