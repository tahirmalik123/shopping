from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer

class CustomerRegister(UserCreationForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


# class Customerform(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TimeInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Password"), strip=False,
                               widget=forms.PasswordInput(
                                   attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class passwordchange(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False,
                                   widget=forms.PasswordInput(
                                       attrs={'autocomplete': 'current-password', 'class': 'form-control', }))
    new_password1 = forms.CharField(label=_("New Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'New-password', 'class': 'form-control', }),
                                    help_text=password_validation.password_validators_help_text_html)
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'New-password', 'class': 'form-control', }))


class pass_reset(PasswordResetForm):
    email = forms.CharField(label=("Email"), max_length=200,
                            widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))

class pass_reset_confirm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'New-password', 'class': 'form-control', }),
                                    help_text=password_validation.password_validators_help_text_html)
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False,
                                    widget=forms.PasswordInput(
                                        attrs={'autocomplete': 'New-password', 'class': 'form-control', }))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'zip_code', 'state']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
     'locality': forms.TextInput(attrs={'class': 'form-control'}),
     'city': forms.TextInput(attrs={'class': 'form-control'}),
    'state': forms.Select(attrs={'class': 'form-control'}),
      'zip_code': forms.NumberInput(attrs={'class': 'form-control'})}