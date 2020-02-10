"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from loanapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

  
    path('api/', include('apiapp.urls', namespace='api')),
    path('projects/', include('projectapp.urls', namespace='projects')),
    path('cassavas/', include('cassavaapp.urls', namespace='cassavas')),

    path('loans/', include('loanapp.urls', namespace='loans')),
    path('dogcats/', include('dogcatapp.urls', namespace='dogcats')),
    path('contacts/', include('contactapp.urls', namespace='contacts')),
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
