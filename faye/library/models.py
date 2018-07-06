import datetime

from django.db import models
from django.utils import timezone

class LibraryObject(models.Model):

	# eventually update the appearance of these in the admin
	title       = models.CharField(max_length=200, default="n/a")
	author      = models.CharField(max_length=200, default="n/a")
	description = models.CharField(max_length=1000, default="n/a")
	pub_date    = models.DateTimeField('date published')
	acq_date    = models.DateTimeField('date acquired')
	ISBN_10     = models.CharField(max_length=20, default="n/a")
	ISBN_13     = models.CharField(max_length=20, default="n/a")
	pages       = models.IntegerField(default=0)
	pages_read  = models.IntegerField(default=0)

	def __str__(self):
		# return first 100 chars of status message as identifier
		return self.title