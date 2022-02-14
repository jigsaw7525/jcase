from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password1',
                  'password2', 'city', 'respondent']
