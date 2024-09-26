from django import forms
from ftplib import MAXLINE

class CreateNewTask(forms.Form):
    title = forms.CharField(label= "Evento", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField (widget=forms.Textarea(attrs={'class':'input'}),label= "Descripción de evento", required=False)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label= "Proyecto", max_length=200,widget=forms.Textarea(attrs={'class':'input'}))
