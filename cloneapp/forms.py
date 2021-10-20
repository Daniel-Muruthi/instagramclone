from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Enter your email',widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    username = forms.CharField(required=True, label='Enter your username',widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password1 = forms.CharField(required=True, label='Enter your password1',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password1'}))
    password2 = forms.CharField(required=True, label='Enter your password2',widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password2'}))


    class Meta:
        model = User
        fields =("username", "email", "password1", "password2")

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