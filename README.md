# project faye

## next steps (general)
- fixing css for mobile (especially when hiding elements), and paring down all css to minimal needed (i.e., genericize)
- including true home buttons in relevant pages
- enabling smart back-paging (i.e., return to proper page of paginator object)
- enabling reasonable sorting methods for library contents (i.e., alphabetical by last name, by pub date, by acq date)
- it might be edifying to include an integrated email form (I don't prefer the idea of comments or posting).
- finalizing production mode image/media serving (should be easy as only admin has privilege)
- actual aesthetic changes to the website (viz images, lettering, justification settings, simple scroll indicators)
- eventually use of the reverse capabilities of many-to-many fields in the library objects
- standardize the hierarchy of page content (i.e., how subheadings interact with info, etc.)
- specialty pages within the library app (keep minimal: e.g., especially recommended, new)
- medium term: separate books and authors into parent and child objects, independently groupable, assignable, etc.
- I can also permit script in posts (safe by how they're uploaded)
- title case should be applied to book titles, and null fields from the google books ping can be handled in populate_books
- book categories aren't currently implemented
- standardize the git flow from local machine to webserver (this seems to have been resolved)

### status updates
- I am debating whether statuses should accept text as clean (and thus render html). the single paragraph format keeps me honest, though a lack of links can hurt
- regardless, statuses should be able to have tags in addition to citations, though these should be strictly limited

### library updates
- need to bring current collection up to date, remove duplicates, and standardize json loading process
- books should show some sort of placeholder for description, remove pages read inclusion, and show rating or something
- ideally there should be a method to reload changes in the database back into the json static file, for maximal redundancy
- changes currently should only be made to the json file!

### produce updates
- the format on the written and visual landing page can be changed to look a little cleaner (maybe float recent tag)
- possibly metacommentary on stories should be allowed (far future). descriptions suffice for now
- enable sorting by different keys (keep it minimal and static; paginated?: no searching: people should be subjected)

### misc app updates
- consider removing transition speeds, so that the whole thing becomes more clicky (currently implemented)
- requent acquisitions section in library app?
- consider a series of regression tests for core functionality; consider automated library reload

## notes (general)
- probably page numbers can be easily passed to individual templates for back-paging
- should back-paging from referenced library objects be enabled? (can always use back gestures)
- admin page aesthetics (e.g., horizontal filter for many to many relations)
- I need to fix title case in book titles, and disply the rest of the fields
- I need to make sure that the certbot requests are not above the allotted frequency
- git ssh key needs authenticating

## deployment notes (and personal reminders)
- currently I am being very lax with secret key storage and file transfer protocols
- hosting currently moves key elsewhere and uses let's encrypt and certbot for https
- commands for my own memory: `sudo supervisorctl restart faye` (or `reread` or `update` or `status`), `sudo service nginx restart`
- files for server care and upkeep include `/etc/supervisor/conf.d/faye.conf` and `gunicorn_start` and some linking in `/etc/nginx/...`
- currently https is not enabled nor supported, and domain has not been pointed to the proper url
- when pulled, static files should be collected by `python3 manage.py collectstatic`
- when reloading the library `python3 manage.py flush` followed by `createsuperuser` and `populate_books`
