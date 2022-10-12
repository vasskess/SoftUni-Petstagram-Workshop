from django.contrib import admin

from petstagram.pets.models import *


class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Pet, PetAdmin)
