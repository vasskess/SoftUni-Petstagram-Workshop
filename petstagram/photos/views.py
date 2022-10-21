from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home-page")
    context = {"fomr": form}
    return render(request, template_name="photos/photo-add-page.html", context=context)


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
