from django.urls import path, include

from petstagram.photos.views import *

urlpatterns = [
    path("add/", add_photo, name="add-photo"),
    path("<int:pk>/", include([
        path("", detail_photo, name="detail-photo"),
        path("edit/", edit_photo, name="edit-photo"),
    ])),
]
