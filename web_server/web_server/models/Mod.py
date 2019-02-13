from django.db import models

class Mod(models.Model):
    github_username = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    github_id = models.CharField(max_length=30)
    is_auth = models.BooleanField(default=False)
    is_maintainer = models.BooleanField(default=False)
    created_at = models.DateField()
