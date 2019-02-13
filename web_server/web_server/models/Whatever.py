from django.db import models

class User(models.Model):
    github_username = models.CharField(max_length=30)
    id = models.IntField(primary_key=TRUE)
    github_id = models.CharField(max_length=30)
    is_auth = models.BooleanField(default=False)
    is_maintainer = models.BooleanField(default=False)
    created_at = models.DateField()
