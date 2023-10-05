from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=100,unique=True)
    position=models.TextField()
    image=models.ImageField(upload_to='teams',blank=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    galleryimg=models.ImageField(upload_to='gallery',blank=True)

class Blog(models.Model):
    blogimg=models.ImageField(upload_to='blog',blank=True)
    question=models.TextField()
    desc=models.TextField()
