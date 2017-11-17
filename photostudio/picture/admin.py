from django.contrib import admin
from .models import Post, tags, User
# Register your models here.

admin.site.register(Post)
admin.site.register(User)
admin.site.register(tags)
