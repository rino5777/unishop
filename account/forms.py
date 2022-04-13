from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):   # игнорирование стандартных стилей 
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Password' , 'rows': 1, })
        self.fields['password2'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Confirm Password' , 'rows': 1, })
        self.fields['email'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'E-mail Address' , 'rows': 1, })
        self.fields['username'].widget.attrs.update({ 'class': 'form-control', 'placeholder': 'Username' , 'rows': 1, })


    class Meta:
        model = User
        fields = [ 'username',  'email',  'password1', 'password2',]

        # widgets =  {
        #     'username': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'First Name' , 'rows': 1, }),
        #     #'LastName': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Last Name' , 'rows': 1, }),
        #     'email': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'E-mail Address' , 'rows': 1, }),
        #     #'PhoneNumber': forms.TextInput( attrs={'class': 'form-control', 'placeholder': 'Phone Number' , 'rows': 1, }),
            
        #     'password2': forms.PasswordInput( attrs={'class': 'form-control', 'placeholder': 'Confirm Password' , 'rows': 1, }),
        # }