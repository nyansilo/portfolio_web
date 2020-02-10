from django.urls import path
from . import views


app_name = 'projectapp'

urlpatterns = [
    path('' , views.projectlist , name='project_list') , 
    path('<slug:project_slug>' , views.projectdetail , name='project_detail') , 
    #path('<slug:category_slug>' , views.productlist , name='product_list_category') , 
    #path('detail/<slug:product_slug>' , views.productdetail , name='product_detail'),
    #path('allprojects/', views.ProjectListApiView.as_view()),

]