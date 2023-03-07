from django.db import models
from django.utils import timezone
class User(models.Model):
    # TODO add fields
    id = models.IntegerField(primary_key = True)
    github_username = models.CharField(max_length = 30)
    github_id = models.CharField(max_length = 30)
    is_auth = models.BooleanField(default = False)
    is_maintainer = models.BooleanField(default = False)
    created_at = models.DateField(default = timezone.now())
