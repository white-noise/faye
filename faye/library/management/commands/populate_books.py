from django.core.management.base import BaseCommand
from library.models import LibraryObject

import json

class Command(BaseCommand):
	args = ""
	help = ""

	def _populate(self):

		# use path as according to manage.py
		json_data = open("library/static/library/scrubbed_data.json").read()
		json_obj  = json.loads(json_data)

		# for testing purposes
		print(json_data)
		print("\n")
		print(json_obj[0])
		print("populating...")

	def handle(self, *args, **options):
		self._populate()