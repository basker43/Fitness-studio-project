from django.urls import path
from .views import *

urlpatterns=[
    path('cardiopage/',cardioclient),
    path('cardiotablelist/',cardioclientlist),
    path('cardio/delete/<int:id>/',delete,name='cardio_delete')




]    