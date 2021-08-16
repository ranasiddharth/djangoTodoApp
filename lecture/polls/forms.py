from django import forms
from django.forms import ModelForm
from .models import TodoItem, TodoList

class DateInput(forms.DateInput):
    input_type = 'datetime-local'

class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        widgets = {'due_date': DateInput()}
        exclude = ['todo_list']
