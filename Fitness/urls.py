from django.urls import path
from .views import *

urlpatterns=[
    path('gym/',index),
    path('home/',homepage),
    path('fitness/',fitnesspage),
    path('yogaclients/',yogaclient),
    path('yogaclientlist/',yogaclientlist),
    path('yoga/delete/<int:id>/',delete,name='yoga_delete'),
]