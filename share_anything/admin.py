from django.contrib import admin
from .models import (
    UserProfileModel,
    PostModel,
    likeModel,
    FollowModel
)

# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(PostModel)
admin.site.register(likeModel)
admin.site.register(FollowModel)