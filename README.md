# project faye

## next steps
- fixing css for mobile, and paring down all css to minimal needed (i.e., genericize)
- specifically some of the :hover behavior is wonky right now
- including home buttons in relevant pages
- enabling smart back-paging (i.e., return to proper page of paginator object)
- enabling reasonable sorting methods for library contents (i.e., alphabetical by last name, by pub date, by acq date)
- it might be edifying to include an integrated email form (I don't prefer the idea of comments or posting).
- finalizing production mode image/media serving (should be easy as only admin has privilege)
- actual aesthetic changes to the website (viz images, lettering, justification settings, simple scroll indicators)
- eventually use of the reverse capabilities of many-to-many fields in the library objects
- standardize the hierarchy of page content (i.e., how subheadings interact with info, etc.)
- specialty pages within the library app (keep minimal: e.g., especially recommended, new)
- medium term: separate books and authors into parent and child objects, independently groupable, assignable, etc.

## notes
- probably page numbers can be easily passed to individual templates for back-paging
- should back-paging from referenced library objects be enabled? (can always use back gestures)
- admin page aesthetics (e.g., horizontal filter for many to many relations)

## deployment notes
- currently I am being very lax with secret key storage and file transfer protocols
- hosting currently moves key elsewhere and uses let's encrypt and certbot for https
- commands for my own memory: `sudo supervisorctl restart faye` (or `reread` or `update` or `status`), `sudo service nginx restart`
- files for server care and upkeep include `/etc/supervisor/conf.d/faye.conf` and `gunicorn_start` and some linking in `/etc/nginx/...`
- currently https is not enabled nor supported, and domain has not been pointed to the proper url