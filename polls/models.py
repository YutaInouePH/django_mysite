import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    published_at = models.DateTimeField('Date Published at')
    created_by = models.CharField(max_length = 200, null = True)
    
    @admin.display(
        boolean = True,
        ordering = 'published_at',
        description = 'Published Recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        
        return now - datetime.timedelta(days = 1) <= self.published_at <= now

    def __str__(self):
        return str(self.id) + ":" + self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    created_by = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.id) + ":" + self.choice_text