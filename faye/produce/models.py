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

	cited_works  = models.ManyToManyField('library.LibraryObject', blank=True)

	def __str__(self):
		return self.title

class VisualObject(models.Model):

	title       = models.CharField(max_length=200, default="n/a")
	description = models.CharField(max_length=500, default="n/a")
	pub_date    = models.DateTimeField('date published',default=timezone.now)
	content     = models.ImageField(upload_to='img/', default=None)
	
	cited_works  = models.ManyToManyField('library.LibraryObject', blank=True)

	def __str__(self):
		return self.title