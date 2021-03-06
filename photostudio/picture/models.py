from __future__ import unicode_literals
from django.db import models

# Create your models here.


class tags(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.name

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    @classmethod
    def display_tags(cls):
        all_tags = tags.objects.all()
        return all_tags

    @classmethod
    def search_for_tag(cls, search_term):
        tags = cls.objects.filter(name__icontains=search_term)
        return tags


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=30)
    image_link = models.CharField(max_length=60)
    tags = models.ManyToManyField(tags)
    user = models.ForeignKey(User)
    post_image = models.ImageField(upload_to='posts/', null=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()


@classmethod
def search_by_title(cls, search_term):
    picture = cls.objects.filter(title__icontains=search_term)

    return picture
