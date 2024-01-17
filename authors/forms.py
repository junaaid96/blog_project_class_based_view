from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# here forms.ModelForm is a class that will convert our model into a form. We can also use forms.Form to create a form from scratch. AuthorForm is the name of our form.

# class AuthorForm(forms.ModelForm):
#     # we use Meta class to specify the model we are using and the fields we want to include in our form
#     class Meta:
#         model = Author
#         fields = '__all__'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ChangeUserDataForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
