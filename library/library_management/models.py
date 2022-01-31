from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/4.0/ref/models/fields/#


BOOK_GENRE = (
    ('scifi', 'Sci-Fi'),
    ('history', 'History'),
    ('classics', 'Classics'),
    ('horror', 'Horror'),
    ('kids', 'Kids'),
)


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    name = models.CharField(max_length=512)
    year_published = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    genre = models.CharField(max_length=128, choices=BOOK_GENRE, null=True, blank=True)
    book_type = models.PositiveSmallIntegerField(default=1, null=False, blank=False)
    copies_num = models.PositiveSmallIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.name} by {self.author}"

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Loan(models.Model):
    customer = models.ForeignKey(Author, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()