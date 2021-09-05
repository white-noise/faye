# project faye

## major modifications planned
- additional property for status posts that indicate whether they are writing or research focused, with easy (perhaps colored) indicator; using enumeration sub-classes and a choices field should be the best way to do this, with opportunities available to later expand the relevant data types
- what remains is how to select and test for this choice property within a form
- use of the subsection marker where appropriate
- consistent use of color, indentation, rules, and arrows
- cleaner date/posting indication for writing
- paring down library subsection to include only a small selection of books with longer inclusions/attached information
- Should we allow for some flag for whether an article is displayed or not? If logged in, we could allow for viewing, but also maybe we can keep things pretty casual
- Embedded images in posts could be fun, but would involve modifying the body of the post object with a secondary model

## next steps (general)
- including true home buttons in relevant pages
- enabling smart back-paging (i.e., return to proper page of paginator object)
- enabling reasonable sorting methods for library contents (i.e., alphabetical by last name, by pub date, by acq date)
- it might be cool to include an integrated email form (I don't prefer the idea of comments)
- actual aesthetic improvements to the website (viz. images, lettering)
- use of many to many relations to enable quick intuitive linkages from produce to library
- specialty pages within the library app with small reviews and ratings (keep minimal: e.g., especially recommended, new)
- title case should be applied to book titles...
- population of books should have its own flush method, always drawing from local json
- each book field should eventually see some use (e.g., category)

### status updates
- statuses now accept input as safe, and this should support linking and formatting, etc.
- statuses still need tags, but to be honest I like the eclecticism

### library updates
- need to bring current collection up to date, remove duplicates, and standardize json loading process
- flush and repopulate flow can be improved, along with selective templates for when fields are unused or unknown
- changes should only be made to the json file! this is the ideal schema

### produce updates
- possibly meta-commentary on stories should be allowed (far future). descriptions suffice for now
- enable sorting by different keys (keep it minimal and static; paginated?: no searching: people should be subjected)

### misc app updates
- recent acquisitions section in library app? or 'currently reading' pinned section
- consider a series of regression tests for core functionality; consider automated library reload

## notes (general)
- probably page numbers can be easily passed to individual templates for back-paging
- should back-paging from referenced library objects be enabled? this gets hairy and chrome et al. can handle it well enough.
- admin page aesthetics (e.g., horizontal filter for many to many relations)
- title case!
- I need to make sure that the certbot requests are not above the allotted frequency
- can and should cron on the webserver be used to make periodic pushes?

## deployment notes (and personal reminders)
- currently I am being very lax with secret key storage and file transfer protocols. whoops. need to change this if I ever write posts
- hosting currently moves key elsewhere and uses let's encrypt and certbot for https
- commands for my own memory: `sudo supervisorctl restart faye` (or `reread` or `update` or `status`), `sudo service nginx restart`
- files for server care and upkeep include `/etc/supervisor/conf.d/faye.conf` and `gunicorn_start` and some linking in `/etc/nginx/...`
- https is currently supported (keep an eye on hook used by cron tab program for 90 day updates)
- when pulled, static files should be collected by `python3 manage.py collectstatic`
- when reloading the library `python3 manage.py flush` followed by `createsuperuser` and `populate_books`
