from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
#from django.http import HttpResponse

#def homepageview(request):
    #return HttpResponse("Hello world")

class Homepageview(TemplateView):
    template_name: str="home.html"
class Aboutpageview(TemplateView):
    template_name: str="about.html"