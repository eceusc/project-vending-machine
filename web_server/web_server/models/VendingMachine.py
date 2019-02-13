from django.db import models


class VendingMachine(models.Model):
    id = models.IntegerField(primary_key=True)
    last_online = models.DateTimeField()
