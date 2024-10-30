from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=['%Y-%m-%d'],  # Specify your desired date format here
        widget=forms.DateInput(attrs={'type': 'date'})  # HTML5 date picker
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status',
                  'due_date', 'priority', 'category']

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
