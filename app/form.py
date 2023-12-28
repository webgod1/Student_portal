from django import forms
from .models import *

class NoteForms(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeWork(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ['title', 'due', 'subject', 'description', 'finished']

class Youtube(forms.Form):
    text = forms.CharField(max_length=200, label='Enter your search ')

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ['desription']

class Todo_form(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description']