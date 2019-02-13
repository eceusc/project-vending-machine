from django.db import models

class Contributions(models.Model):
    id = models.IntegerField()
    type = models. # not too sure what to put here. maybe Field.choices?
    contributor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    approval = models.IntegerField()
