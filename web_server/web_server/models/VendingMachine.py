from django.db import models


class VendingMachine(models.Model):
    id = models.IntegerField(max_length=5,primary_key=True)
    last_online = models.DateTimeField()
