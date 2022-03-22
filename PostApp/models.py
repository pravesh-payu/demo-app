from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from UserApp.models import User


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def update_post_count_to_user(sender, instance, created, **kwargs):
    return User.objects.post_count_update()


post_save.connect(update_post_count_to_user, sender=Post)
