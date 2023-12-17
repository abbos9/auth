from django.forms import ModelForm

from user.models import User


class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'image', 'phone', 'job', 'about_me', 'username', 'password']

