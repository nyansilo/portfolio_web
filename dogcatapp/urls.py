from django.urls import path, include
from . import views

app_name = 'dogcatapp'

urlpatterns = [
	path('', views.dogcatform, name='dogcat_form'),
] 
