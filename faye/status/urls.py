from django.urls import path

# import from the containing folder
from . import views

# add a namespace so that multiple apps
# are differentiated between
# make sure to change definitions in template
# e.g., status:individual
app_name = "status"

urlpatterns = [
	# example: /status/
	path("", views.index, name="index"),
	# example: /status/1/
	path("individual/<int:status_id>/", views.individual, name="individual"),
]