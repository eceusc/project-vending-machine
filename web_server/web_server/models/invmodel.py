from django.db import models

class invmodel(models.Model):
    id = models.IntegerField(primary_key=True)
    machine = models.IntegerField()
    item = models.IntegerField()
    transaction = models.IntegerField()
