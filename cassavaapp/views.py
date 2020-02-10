from django.shortcuts import render
from django.contrib import messages


from .forms import CassavaForm
from .models import CassavaModel

import pickle
from keras import backend as K
import joblib
import numpy as np
from sklearn import preprocessing
from keras.preprocessing import image
import pandas as pd
from collections import defaultdict, Counter
import base64



""" CASSAVA PREDICT FUNCTION """

def cassavapredict(uploadedImg):
	try:
		mdl        = joblib.load("/Users/pro/Documents/python/MyDjangoProjects/Portfolio/cassavaapp/cassava_model.pkl")
		test_image = image.load_img(uploadedImg, target_size = (64, 64))
		test_image = image.img_to_array(test_image)
		test_image = np.expand_dims(test_image, axis = 0)
		pred       = mdl.predict(test_image)
		pred = [np.argmax(pred[i]) for i in range(len(pred))]

		for i in range(len(pred)):
		    if pred[i] == 0:
		        pred[i] = 'cbb'
		    if pred[i] == 1:
		        pred[i] = 'cbsd'
		    if pred[i] == 2:
		        pred[i] = 'cgm'
		    if pred[i] == 3:
		        pred[i] = 'cmd'
		    if pred[i] == 4:
		        pred[i] = 'healthy'

		K.clear_session()
		return pred[i]

	except ValueError as e:
		return (e.args[0])  


""" CASSAVA FORM FUNCTION """

def cassavaform(request):
	if request.method=='POST':
		formdata=CassavaForm(request.POST, request.FILES)
		if formdata.is_valid():
			name     =  formdata.cleaned_data['name']
			imgfile = formdata.cleaned_data['imagefile']
			uploadedImg = imgfile
			name = name.capitalize()
			#b64_img = base64.b64encode(imgfile.file.read())
			print(uploadedImg)
			prediction = cassavapredict(uploadedImg)
			print(prediction)
			messages.success(request,'Hello {} your prediction is {}'.format(name,prediction))
			
	formdata=CassavaForm()

	template = 'cassava/cassava_form.html'
	context = {'form_data' : formdata }
				
	return render(request, template, context )

