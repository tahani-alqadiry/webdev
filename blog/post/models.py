from django.db import models
from user_profile.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    release_date = models.DateTimeField(auto_now_add=True)

    # post_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

# class User_blog(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     created_date = User.joined
#     blog_name = User.blog_name
#     is_active = models.BooleanField(default=True)
#     header = models.ImageField(upload_to='blog_imgs/')
#
#     def __str__(self):
#         return self.blog_name

