from django.forms import ModelForm
from .models import *

class cardio_client(ModelForm):
    class Meta:
           model=Cardio
           fields='__all__'
