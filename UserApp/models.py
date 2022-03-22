from django.core.paginator import Paginator
from django.db import models


# Create your models here.
def update_post_count():
    print("Update Post count started")
    queryset = User.objects.all()

    paginator = Paginator(queryset, 1000)

    for page_number in paginator.page_range:
        page = paginator.page(page_number)

        for user in page.object_list:
            posts_count = user.post_set.count()
            user.posts_count = posts_count
            user.save()
            print("Update completed for user=", user.get_full_name())


class UserManager(models.Manager):
    def post_count_update(self):
        return update_post_count()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    posts_count = models.IntegerField(default=0)
    # posts = models.One('Post')

    objects = UserManager()

    def get_full_name(self):
        return self.firstname + " " + self.lastname
