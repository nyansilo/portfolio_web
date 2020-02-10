from django.urls import path, include
from . import views
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('loanApi', views.ApprovalsView)

app_name = 'loanapp'

urlpatterns = [
	path('', views.loanform, name='loan_form'),
	#path('form/', views.loanform2, name='loan_form2'),
	#path('api/', include(router.urls)),
    #path('status/', views.ApproveRejectApiView.as_view()),
 
] 
