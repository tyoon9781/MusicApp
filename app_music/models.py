from django.db import models


# Create your models here.
class Diary(models.Model):
    user = models.CharField(max_length=15)
    title = models.CharField(max_length=63)
    create_datetime = models.DateTimeField(auto_now_add=True)
    paragraph = models.CharField(max_length=255)