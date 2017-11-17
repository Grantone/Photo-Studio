from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=30)
    image_link = models.CharField(max_length=250)
    image_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
