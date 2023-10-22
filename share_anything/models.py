from typing import Any
from django.db import models
from django.contrib.auth.models import User


# UserProfile model to extend the built-in User model
class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=False, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/profile', blank=False, default='profile-img.jpg')
    profile_bg_picture = models.ImageField(
        upload_to='profile_pics/bg', blank=False, default='default-user-bg.jpg')

    def __str__(self):
        return self.user.username


# Post model for user-generated content
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discription_text = models.TextField(max_length=500, blank=True, default='')
    code_text = models.TextField(max_length=500, blank=True, null=True, default='null')
    image = models.ImageField(
        upload_to='user_post_image/', blank=True, null=True, default='null')
    # options
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'


# Like model to track likes on posts
class likeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Follow model to handle user relationships (followers/following)
class FollowModel(models.Model):
    follower = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
