from django.core.validators import MinValueValidator
from django.db import models

from petstagram.pets.models import Pet


class Photo(models.Model):
    photo = models.ImageField()
    description = models.TextField(max_length=300, validators=(MinValueValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
