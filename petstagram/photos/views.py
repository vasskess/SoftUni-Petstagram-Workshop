from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home-page")
    context = {"form": form}
    return render(request, template_name="photos/photo-add-page.html", context=context)


def detail_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {"photo": photo, "likes": likes, "comments": comments}
    return render(request, template_name="photos/photo-details-page.html", context=context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(instance=photo)
    if request.method == "POST":
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("detail-photo", pk)
    context = {"form": form}
    return render(request, template_name="photos/photo-edit-page.html", context=context)
