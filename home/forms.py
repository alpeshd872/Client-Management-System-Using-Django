from django.forms import ModelForm
from .models import *


class orderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'


class updateForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
