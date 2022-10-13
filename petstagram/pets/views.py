from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, template_name="pets/pet-add-page.html")


def details_pet(request, username, pet_name):
    context = {}
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    context["pet"] = pet
    context["all_photos"] = all_photos

    return render(request, template_name="pets/pet-details-page.html", context=context)


def edit_pet(request, username, pet_name):
    return render(request, template_name="pets/pet-edit-page.html")


def delete_pet(request, username, pet_name):
    return render(request, template_name="pets/pet-delete-page.html")
