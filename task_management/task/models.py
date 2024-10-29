from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    category = models.CharField(max_length=50, blank=True)
    # Each task belongs to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
