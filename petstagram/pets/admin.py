from django.contrib import admin

from petstagram.pets.models import *


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
