from django.forms import ModelForm
from .models import Eventos

class EventForm (ModelForm):
    class Meta:
        model =Eventos
        fields = ['title', 'description', 'important']
    
        