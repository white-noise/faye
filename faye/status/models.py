import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# the main process:
# change your models (in models.py).
# run python manage.py makemigrations to create migrations for those changes
# run python manage.py migrate to apply those changes to the database.

class StatusObject(models.Model):

    class StatusType(models.TextChoices):
        TECH_STATUS = 'T', _('Technical Status')
        LIT_STATUS  = 'L', _('Literature Status')
        NEUT_STATUS = 'N', _('Neutral Status')

    status_type = models.CharField(
        max_length = 1,
        choices    = StatusType.choices,
        default    = StatusType.NEUT_STATUS,
    )

    status_title = models.CharField(max_length=200, default="update")
    description  = models.CharField(max_length=500, default="no description")
    status_text  = models.TextField(max_length=5000, default="There is no text.")
    pub_date     = models.DateTimeField('date published', default=timezone.now)

    cited_works  = models.ManyToManyField('library.LibraryObject', blank=True)

    def __str__(self):
        return self.status_title
