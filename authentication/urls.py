from django.urls import path
from .views import (
    UserCreationFormView,
    UserLoginView,
    UserLogoutView
)

urlpatterns = [
    path('sign-up/', UserCreationFormView.as_view(), name='sign-up-page'),
    path('sign-in/', UserLoginView.as_view(), name='sign-in-page'),
    path('sign-out/', UserLogoutView.as_view(), name='sign-out-page'),
]
