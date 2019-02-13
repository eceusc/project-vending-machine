from django.db import models
from web_server.models.Owner import Owner

class Doggo(models.Model):
    name = models.CharField(max_length=30)
    is_good = models.BooleanField(default=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
