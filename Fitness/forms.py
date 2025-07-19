from django.forms import ModelForm
from .models import *

class yoga_client(ModelForm):
    class Meta:
           model=Yoga
           fields='__all__'

