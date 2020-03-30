from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views import View
# Create your views here.

def home(request):
    return render(request,'Cylus/home.html',{})

class ContactView(View):
    def get(self,request):
        return render(request,'Cylus/contact.html',{})

class AboutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'Cylus/about.html',{})