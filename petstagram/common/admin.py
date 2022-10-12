from django.contrib import admin

from petstagram.common.models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id",)
