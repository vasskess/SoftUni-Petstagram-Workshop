from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photo(request):
    return render(request, template_name="photos/photo-add-page.html")


def detail_photo(request, pk):
    context = {}
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context["photo"] = photo
    context["likes"] = likes
    context["comments"] = comments

    return render(request, template_name="photos/photo-details-page.html", context=context)


def edit_photo(request, pk):
    return render(request, template_name="photos/photo-edit-page.html")
