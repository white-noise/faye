import datetime

from django.db import models
from django.utils import timezone

# the main process:
# change your models (in models.py).
# run python manage.py makemigrations to create migrations for those changes
# run python manage.py migrate to apply those changes to the database.

class StatusObject(models.Model):

	status_title = models.CharField(max_length=200, default="update")
	description  = models.CharField(max_length=500, default="no description")
	status_text  = models.TextField(max_length=5000, default="There is no text.")
	pub_date     = models.DateTimeField('date published', default=timezone.now)

	cited_works  = models.ManyToManyField('library.LibraryObject', blank=True)

	def __str__(self):
		return self.status_title
