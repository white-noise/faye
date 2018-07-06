import datetime

from django.db import models
from django.utils import timezone

# the main process:
# change your models (in models.py).
# run python manage.py makemigrations to create migrations for those changes
# run python manage.py migrate to apply those changes to the database.

class StatusObject(models.Model):

	# eventually update the appearance of these in the admin
	status_title = models.CharField(max_length=200, default="update")
	status_text  = models.CharField(max_length=1000)
	pub_date     = models.DateTimeField('date published')

	def recently_published(self):
		is_recent = self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		is_past   = self.pub_date <= timezone.now()
		return is_recent and is_past

	def __str__(self):
		# return first 100 chars of status message as identifier
		return self.status_title
