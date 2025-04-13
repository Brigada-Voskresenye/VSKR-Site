from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50,blank=False)
    surname = models.CharField(max_length=50,blank=False,null=True)
    birthdate = models.DateField(blank=True,null=True)
    death_date = models.DateField(blank=True, null=True)
    bio = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Автор"

class Genre(models.Model):
    name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Жанр"

class Book(models.Model):
    title = models.CharField(max_length=150, blank=False)
    date_of_create = models.DateField(blank=True, null=True)
    author = models.ForeignKey(Author,
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               verbose_name="Автор")
    genre = models.ForeignKey(Genre,
                               on_delete=models.SET_NULL,
                               blank=True,
                               null=True,
                               verbose_name="Жанр")

    def __str__(self):
        return f"{self.title} {self.date_of_creation} {self.author} {self.genre}"

    class Meta:
        verbose_name = "Жанр"