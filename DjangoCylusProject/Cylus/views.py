from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    #assert isinstance(request, HttpResponse)
    return render(request,
                  'Cylus/index.html',
                  {
                    'tilte':'Home',
                    'year': datetime.now().year,
                    'content':"Here us some content"

                  })