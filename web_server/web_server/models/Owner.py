from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=30)
