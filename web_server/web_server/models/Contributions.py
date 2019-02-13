from django.db import models
from enum import Enum

class ContributorType(Enum):
    AD = "Admin"
    ME = "Member"


class Contributions(models.Model):
    id = models.IntegerField()
    type = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in ContributorType]
    )
    contributor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    approval = models.IntegerField()
