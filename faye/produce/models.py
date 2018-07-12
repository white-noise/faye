import datetime

from django.db import models
from django.utils import timezone

# make these inherit from one art object class that can be
# displayed safely in a menu with fields such as title, description, and pub_date

class WrittenObject(models.Model):

	title       = models.CharField(max_length=200, default="n/a")
	description = models.CharField(max_length=500, default="n/a")
	pub_date    = models.DateTimeField('date published',default=timezone.now)
	word_count  = models.IntegerField(default=0)
	content     = models.TextField(default="n/a")

	def __str__(self):
		return self.title

class VisualObject(models.Model):

	title       = models.CharField(max_length=200, default="n/a")
	description = models.CharField(max_length=500, default="n/a")
	pub_date    = models.DateTimeField('date published',default=timezone.now)
	path        = models.CharField(max_length=500, default="n/a")
	# eventually this will be an ImageField or a FileField (permitting uploads)

	def __str__(self):
		return self.title