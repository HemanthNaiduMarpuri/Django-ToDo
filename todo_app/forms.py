from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Task

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Enter Password"})
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Confirm Password"})
    )

    class Meta:
        model = User
        fields = ('username', 'email',)

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="email",
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control',  'placeholder': 'Enter Password'})
    )

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','important','deadline')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add a Task'}),
            'important' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'deadline' : forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        }