from django.db import models

class transaction(models.Model):
	# do stuff
	user_id = models.IntegerField()
	user = models.IntegerField()
	timestamp = models.DateField()
	# test
