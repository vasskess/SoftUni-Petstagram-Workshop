from django.urls import path
from petstagram.common.views import *

urlpatterns = (
    path("", home_page, name="home-page")
)
