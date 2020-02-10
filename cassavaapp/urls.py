from django.urls import path, include
from . import views

app_name = 'cassavaapp'

urlpatterns = [
	path('', views.cassavaform, name='cassava_form'),
	
] 
