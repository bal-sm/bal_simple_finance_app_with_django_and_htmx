from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_contact_form/", views.create_contact_form, name="create_contact_form"),
]
