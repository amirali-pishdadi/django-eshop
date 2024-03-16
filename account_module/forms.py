from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True,
                                 widget=forms.TextInput(attrs={"class": "txt", "placeholder": "نام"}))
    last_name = forms.CharField(max_length=150, required=True,
                                widget=forms.TextInput(attrs={"class": "txt", "placeholder": "نام خانوادگی"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "txt", "placeholder": "ایمیل", "type": "email"}),
                             required=True, validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ])
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={"class": "txt", "placeholder": "رمز عبور", "type": "password"}),
                               validators=[validators.MaxLengthValidator(100)])

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "txt", "placeholder": "تکرار رمز عبور", "type": "password"}),
        required=True,
        validators=[validators.MaxLengthValidator(100)])

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password == confirm_password:
            return confirm_password
        raise ValidationError("کلمه عبور و تکرار کلمه عبور مغایرت دارد")


class LoginForm(forms.Form):
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(
        attrs={"class": "txt", "placeholder": "ایمیل", "type": "email"}), validators=[
        validators.MaxLengthValidator(100),
        validators.EmailValidator,
    ])

    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(
        attrs={"class": "txt", "placeholder": "رمز عبور", "type": "password"}),
                               validators=[validators.MaxLengthValidator(100)])


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(
        attrs={"class": "txt", "placeholder": "ایمیل خود را وارد کنید ...", "type": "email"}), validators=[
        validators.MaxLengthValidator(100),
        validators.EmailValidator,
    ])


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(
        attrs={"class": "txt", "placeholder": "رمز عبور جدید خود را وارد کنید ...", "type": "password"}), validators=[
        validators.MaxLengthValidator(100),
        validators.EmailValidator,
    ])


class UserInfoPageModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "avatar", "about_user", "address"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "txt", "placeholder": "نام"}),
            "last_name": forms.TextInput(attrs={"class": "txt", "placeholder": "نام خانوادگی"}),
            "phone_number": forms.TextInput(attrs={"class": "txt", "placeholder": "شماره تلفن ( بدون صفر )"}),
            "avatar": forms.FileInput(attrs={"class": "txt", "placeholder":  "تصویر پروفایل"}),
            "address": forms.TextInput(attrs={"class": "txt", "placeholder": "آدرس"}),
            "about_user": forms.Textarea(attrs={"class": "txt--textarea", "placeholder": "درباره کاربر"}),
        }
