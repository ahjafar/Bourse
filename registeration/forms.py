from django import forms
#from .models import User

class NewUserForm(forms.Form):
    username=forms.CharField(max_length=255,
                            label='Your username:',
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(max_length=255,
                            min_length=8,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))

