from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# defining the categories model


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# defining the Task model


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),

    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='medium')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    # Each task belongs to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
