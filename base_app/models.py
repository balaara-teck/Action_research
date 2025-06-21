# models.py

from django.db import models

class FileModel(models.Model):
    TOPIC_CHOICES = [
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('Languages', 'Languages'),
        ('Social', 'Social Studies'),
    ]

    topic = models.CharField(max_length=100)
    field = models.CharField(max_length=100,choices=TOPIC_CHOICES, default='General')
    researcher = models.CharField(max_length=200)
    file = models.FileField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} \n By {self.researcher}"
    
