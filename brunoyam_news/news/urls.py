from django.urls import path
from news.views import index,learning
urlpatterns = {path('index/', index),
               path('learning/',learning),}