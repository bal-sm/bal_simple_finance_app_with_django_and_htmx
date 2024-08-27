from django.shortcuts import redirect
from django.urls import path

from . import views

urlpatterns = [
    path("", lambda _: redirect("create_contact_form"), name="index"),
    path("create_contact_form/", views.create_contact_form, name="create_contact_form"),
]
