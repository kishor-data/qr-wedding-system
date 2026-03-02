from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/<int:id>/", views.event_detail, name="event_detail"),
    path("create-admin/", views.create_admin),
]