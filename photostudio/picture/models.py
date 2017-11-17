from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    image_link = models.CharField(max_length=60)
    post_image = models.ImageField(upload_to='posts/', null=True)
    tags = models.ManyToManyField(tags)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    @classmethod
    def get_posts(cls):
        posts = cls.posts.all()

        return posts


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()

    @classmethod
    def get_users(cls):
        users = cls.objects.all()

        return users
