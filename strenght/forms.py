from django.forms import ModelForm
from .models import *

class Strength_client(ModelForm):
    class Meta:
           model=Strength
           fields='__all__'
