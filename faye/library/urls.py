from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:library_id>/", views.individual, name="individual"),
]