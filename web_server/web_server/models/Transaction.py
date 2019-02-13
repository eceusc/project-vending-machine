from django.db import models

class Transaction(models.Model):
    id = models.IntField(primary_key = True)
    User = models.CharField(max_length = 30)
    timestamp = models.DateField()
