from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Specify your desired date format here
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status',
                  'due_date', 'priority', 'category']
