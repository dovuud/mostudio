from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract =True

class Post(TimeStampedModel):
    title =models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class About(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Pricing(TimeStampedModel):
    photos = models.CharField(max_length=212)
    processing = models.CharField(max_length=212)
    type_camera = models.CharField(max_length=212)
    resolution = models.CharField(max_length=212)
    term = models.CharField(max_length=212)
    price = models.CharField(max_length=212)

    def __str__(self):
        return self.photos
