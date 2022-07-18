# urls file for app pages 

from django.urls import path
from .views import Homepageview,Aboutpageview

urlpatterns = [
     path('about/', Aboutpageview.as_view(),name="about"),
    path('', Homepageview.as_view(),name="home"),
]
