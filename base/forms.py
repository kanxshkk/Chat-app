from django.forms import ModelForm
<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

=======
from .models import Room
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
<<<<<<< HEAD
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
=======
        exclude = ['host','participants']
>>>>>>> 3484baaddb60d1adf35712eb69ed156742d37cec
