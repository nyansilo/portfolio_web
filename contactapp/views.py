from django.shortcuts import render
from .models import Contacts
from django.shortcuts import get_object_or_404
# Create your views here.

def contactinfo(request):

    contactinfo = Contacts.objects.all()
    template = 'contact/contact_us.html'
    context = {'contact_info' : contactinfo }

    return render(request , template , context)