from django.db import models

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=255, blank=False, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50, blank=True)
    author_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.author_name


class Quote(models.Model):
    quote_name = models.TextField(unique=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return f'"{self.quote_name}" - {self.author_name}'


class Tag(models.Model):
    tags_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.tags_name
