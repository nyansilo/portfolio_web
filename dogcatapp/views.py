from django.shortcuts import render
from django.contrib import messages

from .models import DogCatModel
from .forms import DogCatForm


import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
from keras.preprocessing import image
import pandas as pd
from collections import defaultdict, Counter
import base64



"""DOG OR CAT FUNCTION """

def dogorcat(uploadedImg):
	try:
		mdl        = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/dogcatapp/dogcat_model.pkl")
		test_image = image.load_img(uploadedImg, target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		result     = mdl.predict(test_image)
		
		if result[0][0] == 1:
			prediction = '狗'
			predict = 'doggg'
		else:
			prediction = '猫'
			predict = 'cattt'   	
		K.clear_session()
		return prediction

	except ValueError as e:
		return (e.args[0])    


"""DOGCAT FORM FUNCTION """

def dogcatform(request):
	if request.method=='POST':
		formdata=DogCatForm(request.POST, request.FILES)
		if formdata.is_valid():
			name     =  formdata.cleaned_data['name']
			imgfile = formdata.cleaned_data['imagefile']
			uploadedImg = imgfile
			name = name.capitalize()
			#b64_img = base64.b64encode(imgfile.file.read())
			print(uploadedImg)
			prediction = dogorcat(uploadedImg)
			print(prediction)
			messages.success(request,'Hello {} your prediction is {}'.format(name,prediction))
			
	formdata=DogCatForm()

	template = 'dogcat/dogcat_form.html'
	context = {'form_data' : formdata }
				
	return render(request, template, context )
