from django.db import models
from django.urls import reverse

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.email

class Carousel(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='carousel/')
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("carouselDetailView", args=[self.slug])

    def __str__(self):
        return self.name
class Banner(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Facts(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img = models.ImageField(upload_to='facts/')

    def __str__(self):
        return self.name

class Features(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    span = models.TextField()
    img = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
class Blog(models.Model):
    name = models.CharField(max_length=200)
    span = models.IntegerField()
    img = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.name

