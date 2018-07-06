from django.core.management.base import BaseCommand
from library.models import LibraryObject
from django.utils import timezone

import json
import datetime

class Command(BaseCommand):
	args = ""
	help = ""

	def _populate(self):

		# use path as according to manage.py
		json_data = open("library/static/library/json/scrubbed_data.json").read()
		json_obj  = json.loads(json_data)

		print("populating...")

		# for testing purposes
		for elem in json_obj:
			authors       = elem["authors"]
			title         = elem["title"]
			categories    = elem["categories"]
			description   = elem["description"]
			pageCount     = elem["pageCount"]
			# publishedDate = elem["publishedDate"] # needs parsing
			ISBN_list     = elem["industryIdentifiers"]

			for index in ISBN_list:
				if index["type"] == "ISBN_10":
					ISBN_10 = index["identifier"]
				elif index["type"] == "ISBN_13":
					ISBN_13 = index["identifier"]
				else:
					ISBN_10 = 0 # default
					ISBN_13 = 0 # default

			pagesRead     = 0 # default
			publishedDate = timezone.now()
			acqDate       = timezone.now() # default

			# create a book object and save to database
			book = LibraryObject(title=title, author=authors, description=description, pub_date=publishedDate, acq_date=acqDate, ISBN_10=ISBN_10, ISBN_13=ISBN_13, pages=pageCount, pages_read=pagesRead,)
			book.save()

			print(authors)
			print(title)
			print("")

		print("populated")

	def handle(self, *args, **options):
		self._populate()