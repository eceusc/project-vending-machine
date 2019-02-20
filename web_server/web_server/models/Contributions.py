from django.db import models
from django.utils import timezone
from enum import Enum
import uuid

class ContributorType(Enum):
    AD = "Admin"
    ME = "Member"


class Contributions(models.Model):
    identification = models.IntegerField()
    contributionType = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in ContributorType]
    )
    contributor = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateField(default=timezone.now())
    approval = models.IntegerField()
