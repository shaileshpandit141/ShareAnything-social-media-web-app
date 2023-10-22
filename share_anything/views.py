from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    PostModel,
    UserProfileModel
)

# Create your views here.
class IndexView(LoginRequiredMixin, View):

    def get(self, request):
        context = dict(
            posts = PostModel.objects.all(),
            loginUser = UserProfileModel.objects.get(user = request.user),
        )
        return render(request, 'share_anything/index.html', context)