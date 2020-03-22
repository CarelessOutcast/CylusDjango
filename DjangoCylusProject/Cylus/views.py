from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views import View
# Create your views here.

def index(request):
    #assert isinstance(request, HttpResponse)
    return render(request,
                  'Cylus/index.html',
                  {
                    'title':'Home',
                    'year': datetime.now().year,
                    'content':"Here us some content",
                    'message':"Here is my mf message"

                  })
def about(request):
    return render(request,'Cylus/about.html',
                  {
                      'title':'About',
                      'content': 'here is the about contact page',
                      'message':'here is a useless message'
                      })
class ContactView(View):
    def get(self,request):
        return render(request,'Cylus.contact.html',{})