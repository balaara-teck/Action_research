from django.db import models

class FileModel(models.Model):
    TOPIC_CHOICES = [
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('Technical', 'Technical'),
        ('Social', 'Social Studies'),
    ]

    topic = models.CharField(max_length=200)  # required field

    field = models.CharField(
        max_length=100,
        choices=TOPIC_CHOICES,
        default='Science',
       
    )

    researcher = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True
    )

    chapter = models.CharField(
        max_length=200,
        default="Loading...",
        blank=True,
        null=True
    )

    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic} {'| ' + self.researcher if self.researcher else ''}"
