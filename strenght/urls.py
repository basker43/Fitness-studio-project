from django.urls import path
from .views import *

urlpatterns=[
    path('bookingss/',strenghtclient),
    path('strengthbooking/',strengthtable),
    path('strength/delete/<int:id>/',delete,name='strength_delete')

]