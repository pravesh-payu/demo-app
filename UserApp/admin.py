from django.contrib import admin

# Register your models here.
from PostApp.models import Post
from UserApp.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
