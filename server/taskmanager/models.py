from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    """ High-level retail chain model"""
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    finish_date = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_author')
    priority = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    private = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='task_like')


class Answer(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text
