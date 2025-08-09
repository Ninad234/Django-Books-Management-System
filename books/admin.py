from django.contrib import admin
from .models import Booksvariety

# Register your models here.
admin.site.register(Booksvariety)


def __str__(self):
    return self.name