from django.urls import path
from petstagram.common.views import *

urlpatterns = (
    path("", home_page, name="home-page"),
    path("like/<int:photo_id>/", like_functionality, name="like"),
)
