from django.db import models

class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    machine = models.IntegerField()
    item = models.IntegerField()
    #transaction = models.idField(id, on__delete=models.CASCADE)
