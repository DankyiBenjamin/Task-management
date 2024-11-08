from django import forms
from .models import Task, Category
from django.core.exceptions import ValidationError
from datetime import date


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Specify your desired date format here
        widget=forms.DateInput(
            # HTML5 date picker
            attrs={'type': 'date', 'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status',
                  'due_date', 'priority', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        status = self.cleaned_data.get('status')
        # checking if the status is set to done
        if status != "done" and due_date < date.today():
            raise ValidationError("The due date cannot be in the past")

        else:
            return due_date

    def __init__(self, *args, **kwargs):
        # Get the user from view
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(
                user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
