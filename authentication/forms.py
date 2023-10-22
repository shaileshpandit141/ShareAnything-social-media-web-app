from django.forms import ModelForm
from django.contrib.auth.models import User

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']