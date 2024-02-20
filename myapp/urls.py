from django.urls import path 
from myapp import views

urlpatterns = [
    path('', views.list_location, name='list_location'), 
]