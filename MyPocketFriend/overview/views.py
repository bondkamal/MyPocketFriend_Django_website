from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return render(request,'overview_html_file/overview_index.html',
   {'title': 'learn Django','cname':'Django'} )

def index(request):
    return render(request,'overview_html_file/index.html'
    )