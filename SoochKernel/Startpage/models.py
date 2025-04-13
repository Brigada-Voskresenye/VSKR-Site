from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100,blank=False)
    surname = models.CharField(max_length=100,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    death_date = models.DateField(blank=True,null=True)
    bio = models.CharField(max_length=400,blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    class Meta:
        verbose_name="author"

class Genre(models.Model):
    name = models.CharField(max_length=100,blank=False)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name="genre"


class Book(models.Model):
    title = models.CharField(max_length=150, blank=False)
    date_of_creation= models.DateField(blank=True,null=True)
    author = models.ForeignKey(Author,
                               on_delete= models.SET_NULL,
                               blank=True,
                               null=True,
                               verbose_name="author")
    genre = models.ForeignKey(Genre,
                              on_delete= models.SET_NULL,
                               blank=True,
                               null=True,
                               verbose_name="genre")
    
    def __str__(self):
        return self.title