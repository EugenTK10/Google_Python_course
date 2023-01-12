from django.db import models

# Create your models here.

class Joburi(models.Model):

    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    type = models.IntegerField()
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.type} -> {self.title} -> {self.url} -> {self.description}"