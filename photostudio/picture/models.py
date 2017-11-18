from __future__ import unicode_literals

from django.db import models

# Create your models here.


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=30)
    image_link = models.CharField(max_length=60)
    post_image = models.ImageField(upload_to='posts/', null=True)
    tags = models.ManyToManyField(tags)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()


@classmethod
def search_by_title(cls, search_term):
    picture = cls.objects.filter(title__icontains=searc_term)
    return picture
