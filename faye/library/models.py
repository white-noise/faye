import datetime

from django.db import models
from django.utils import timezone

# you can import models from other apps
# from produce.models import WrittenObject, VisualObject
# and then use many to one relationship for relvant works?

class LibraryObject(models.Model):

	title       = models.CharField(max_length=200, default="n/a")
	author      = models.CharField(max_length=200, default="n/a")
	description = models.TextField(max_length=1000, default="")
	pub_date    = models.DateTimeField('date published')
	acq_date    = models.DateTimeField('date acquired',default=timezone.now)
	ISBN_10     = models.CharField(max_length=20, default="n/a")
	ISBN_13     = models.CharField(max_length=20, default="n/a")
	pages       = models.IntegerField(default=0)
	pages_read  = models.IntegerField(default=0)
	rating      = models.IntegerField(default=0)

	def __str__(self):
		return "%s_%s"%(self.author, self.title)