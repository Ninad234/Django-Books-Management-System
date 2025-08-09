from django.db import models
from django.utils import timezone

# Create your models here.
class Booksvariety(models.Model):
    BOOKS_TYPE_CHOICE = [
    ('FIC', 'Fiction'),
    ('NF', 'Non-Fiction'),
    ('MYS', 'Mystery'),
    ('SCI', 'Science'),
    ('BIO', 'Biography'),
    ('ROM', 'Romance'),
    ('FANT', 'Fantasy'),
    ('HIS', 'History'),
    ]
    name = models.CharField(max_length=100),
    image = models.ImageField(upload_to='books'),
    date_added = models.DateTimeField(default=timezone.now),
    type = models.CharField(max_length=10,choices=BOOKS_TYPE_CHOICE)