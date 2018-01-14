from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


# class LoginForm(forms.ModelForm):
# 	username = forms.CharField(max_length=30)
# 	password = forms.CharField(widget=forms.PasswordInput, max_length=30, min_length=8)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'password',)