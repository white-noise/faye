from django.urls import path

from . import views

app_name = "produce"

urlpatterns = [
	path("", views.index, name="index"),
	path("written/", views.written, name="written"),
	path("visual/", views.visual, name="visual"),
	path("written/<int:produce_id>/", views.written_individual, name="written_individual"),
	path("visual/<int:produce_id>/", views.visual_individual, name="visual_individual"),
	path("written/capricorn/", views.capricorn, name="capricorn"),
	path("written/email_view/", views.email_view, name="email_view"),
	path("written/ghost_view/", views.ghost_view, name="ghost_view"),
	path("written/sleep_view/", views.sleep_view, name="sleep_view"),
]