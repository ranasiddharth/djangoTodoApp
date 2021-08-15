from django import forms
from django.forms import ModelForm
from .models import TodoItem, TodoList


class TaskForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        exclude = ['todo_list']
