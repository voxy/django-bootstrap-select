from django.conf import settings
from django.db import models

# Create your models here.

class Icon(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name
