from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from accounts.models import CostumUser



class LoginForm(AuthenticationForm):
    

    class Meta:
        model = CostumUser
        fields = {'username','password'}




class SignupForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.ImageField(required=False)
    id_code = forms.CharField(max_length=10)
    class Meta:
        model = CostumUser
        fields = {'username','password1','password2','email'}