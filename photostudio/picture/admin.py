from django.contrib import admin
from .models import Post, User, tags
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(tags)
