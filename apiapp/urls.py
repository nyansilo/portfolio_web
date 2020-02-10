from django.urls import path
from . import views


app_name = 'apiapp'

urlpatterns = [
	path('allprojects/', views.ProjectListApiView.as_view()),
	path('loan/', views.LoanApiView.as_view()),
	path('dogcat/', views.DogCatApiView.as_view()),
	path('cassava/', views.CassavaApiView.as_view()),
]