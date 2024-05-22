from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    published = models.BooleanField(default=False)
    createdAt = models.DateField(auto_now_add=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
