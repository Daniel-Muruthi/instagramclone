from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email',widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    username = forms.CharField(required=True, label='Username',widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password1 = forms.CharField(required=True, label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(required=True, label='Re-type Password',widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'}))


    class Meta:
        model = User
        fields =("username", "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def passwordcheck(self):
        password1 = self.cleaned_data.get("password1")
        password2= self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mistmatch'],
                code='password_mismatch',
            )
        return password2
#This will create the news letter
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')