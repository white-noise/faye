from django.urls import path
from . import views

app_name = "status"

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:status_id>/", views.individual, name="individual"),
]