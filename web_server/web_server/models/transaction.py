from django.db import models
from django.utils import timezone

class transaction(models.Model):
	# do stuff
	user_id = models.IntegerField()
	user = models.IntegerField()
	timestamp = models.DateField(default=timezone.now())
	# test
