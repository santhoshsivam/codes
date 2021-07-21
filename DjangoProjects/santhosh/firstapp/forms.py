from django.forms import ModelForm
from .models import signin   

class signin_form(ModelForm):
    class Meta:
        model = signin
        fields = '__all__'
