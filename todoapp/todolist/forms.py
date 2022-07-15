from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    
    title = forms.CharField(
    	widget=forms.TextInput(
    		attrs={
    		"class": "form-control form-control-lg",
    		"placeholder": "New task ...",
    		}),)