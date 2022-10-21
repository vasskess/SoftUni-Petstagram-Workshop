from django.shortcuts import render, redirect

from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("profile-details", pk=1)

    context = {"form": form}
    return render(request, template_name="pets/pet-add-page.html", context=context)


def details_pet(request, username, pet_name):
    context = {}
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    context["pet"] = pet
    context["all_photos"] = all_photos

    return render(request, template_name="pets/pet-details-page.html", context=context)


def edit_pet(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("details-pet", username, pet_name)
    context = {"form": form}
    return render(request, template_name="pets/pet-edit-page.html", context=context)


def delete_pet(request, username, pet_name):
    return render(request, template_name="pets/pet-delete-page.html")
