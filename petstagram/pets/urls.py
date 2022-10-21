from django.urls import path, include
from petstagram.pets.views import *


urlpatterns = (
    path("add/", add_pet, name="add-pet"),
    path(
        "<str:username>/pet/<slug:pet_name>/",
        include(
            [
                path("", details_pet, name="details-pet"),
                path("edit/", edit_pet, name="edit-pet"),
                path("delete/", delete_pet, name="delete-pet"),
            ]
        ),
    ),
)
