from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import SetPasswordForm
from django import forms
from django.db import transaction
from .models import *

passwordInputWidget = {
    'password': forms.PasswordInput(),
}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = '__all__'
        widgets = [passwordInputWidget]


class LoginForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = ['email', 'password']
        widgets = [passwordInputWidget]

# class AccountRegister(forms.ModelForm):
#     class Meta:
#         model = StudentReg
#         fields = "__all__"


# class StudentSignUpForm(UserCreationForm):
#     admno = forms.CharField(max_length=6,
#                             widget=forms.CharField(attrs={'id': 'admino', 'onkeypress': "admnoValidation()", }))
#     email = forms.EmailField(max_length=200,
#                              widget=forms.EmailInput(attrs={'id': 'mail', 'onkeypress': "emailValidation()", }))
#
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2']
#         widgets = {
#             # 'email': forms.EmailInput(attrs={'class': 'form-control','id':'email_id','onkeyup':"email_validate()",}),
#             'password1': forms.PasswordInput(
#                 attrs={'class': 'form-control', 'id': 'password1', 'onkeyup': "pass1Validate()"}),
#             'password2': forms.PasswordInput(
#                 attrs={'class': 'form-control', 'id': 'password2', 'onkeyup': "pass2Validate()"}),
#
#             # 'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
#             # 'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Gender'}),
#         }
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_client = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         # user.email = self.cleaned_data('email')
#         user.save()
#         client = Client.objects.create(user=user)
#         client.phone_number = self.cleaned_data.get('phone_number')
#         client.address = self.cleaned_data.get('address')
#         client.save()
#         return user
#
#
# class AdvocateSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'onkeyup': "vfname()", 'id': 'fid', }))
#     last_name = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'lid', 'onkeyup': "lname()", }))
#     license_number = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'licid', 'onkeyup': "license()", }))
#     office_address = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'id': 'addressid', 'onkeyup': "address()", }))
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'license_number', 'office_address', 'password1',
#                   'password2']
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={'class': 'form-control', 'id': 'user_id', 'onkeyup': "validate_username()", }),
#             'email': forms.EmailInput(
#                 attrs={'class': 'form-control', 'id': 'email_id', 'onkeyup': "email_validate()", }),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1', 'onkeyup': "pass1()"}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2', 'onkeyup': "pass2()"}),
#
#         }
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_advocate = True
#         user.is_staff = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         advocate = Advocate.objects.create(user=user)
#         advocate.license_number = self.cleaned_data.get('license_number')
#         advocate.office_address = self.cleaned_data.get('office_address')
#         advocate.save()
#         return user
#
#
# class ClientcaseForm(forms.ModelForm):
#     title = forms.CharField()
#     description = forms.Textarea()
#     proof = forms.FileField()
#
#     class Meta:
#         model = Clientcase
#         exclude = ['user']
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']