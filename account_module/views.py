from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .models import *

from .forms import *


# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {"form": register_form}
        return render(request, "account_module/sign-up.html", context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            first_name = register_form.cleaned_data.get("first_name")
            last_name = register_form.cleaned_data.get("last_name")
            email = register_form.cleaned_data.get("email")
            password = register_form.cleaned_data.get("password")
            user: bool = User.objects.filter(email__iexact=email).exists()
            active_code = get_random_string(72)
            username = str(email).split("@")[0]
            if user:
                register_form.add_error("email", "ایمیل وارد شده تکراری میباشد")
            else:
                new_user = User(first_name=first_name, last_name=last_name, email=email, email_active_code=active_code,
                                avatar="../static/img/profile.jpg", username=username)
                new_user.set_password(password)
                new_user.save()
                # todo : send email
                return redirect(reverse("login_page"))
        context = {
            "form": register_form
        }
        return render(request, 'account_module/sign-up.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {"login_form": login_form}
        return render(request, "account_module/sign-in.html", context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error("email", "حساب کاربری شما فعال نشده است")
                else:
                    pass_check = user.check_password(password)
                    if pass_check:
                        login(request, user)
                        return redirect(reverse("home_page"))
                    else:
                        login_form.add_error("password", "رمز عبور شما درست نیست")
            else:
                login_form.add_error("email", "کاربری با مشخصات وارد شده یافت نشد")
        context = {"login_form": login_form}
        return render(request, "account_module/sign-in.html", context)


class ForgetPasswordView(View):
    def get(self, request):
        forget_form = ForgetPasswordForm()
        context = {"forget_pass_form": forget_form}
        return render(request, "account_module/forget_password.html", context)

    def post(self, request: HttpRequest):
        forget_form = ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data.get("email")
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                # todo : send email
                print(user.email_active_code)
                if user.is_active:
                    print(get_random_string(72))
                    return redirect(f"/user/reset-password/{user.email_active_code}")
                else:
                    print("اکانت شما فعال نشده است")
            else:
                forget_form.add_error("email", "کاربری با ایمیل وارد شده یافت نشد !")
        context = {"forget_pass_form": forget_form}
        return render(request, "account_module/forget_password.html", context)


class ResetPasswordView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return HttpResponse("خطا")
        reset_password = ResetPasswordForm()
        context = {"reset_password": reset_password, "user": user}
        return render(request, "account_module/reset_password.html", context)

    def post(self, request: HttpRequest, active_code):
        reset_password = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_password.is_valid():
            if user is None:
                return HttpResponse("خطای یوزر")
            user_pass = reset_password.cleaned_data.get("password")
            user.set_password(user_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            print("password Changed")
            return redirect(reverse("home_page"))
        context = {"reset_password": reset_password}
        return render(request, "account_module/reset_password.html", context)


class ActiveAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                print("اکانت شما فعال شد")
                return redirect(reverse("home_page"))

            else:
                print("اکانت شما فعال بوده است")
                return redirect(reverse("home_page"))
        raise Http404


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("login_page"))


class EditProfileView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            edit_page_form = UserInfoPageModelForm(instance=request.user)
            context = {"edit_page_form": edit_page_form}
            return render(request, "account_module/edit_user_profile.html", context)
        else:
            return redirect(reverse("home_page"))

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(pk=request.user.id).first()
        if current_user:
            edit_form = UserInfoPageModelForm(data=request.POST, files=request.FILES, instance=current_user)
            print(request.POST)
            print(request.FILES)
            avatar = edit_form.cleaned_data["avatar"]
            if edit_form.is_valid():
                edit_form.save(commit=True)
                return redirect(reverse("home_page"))
            else:
                return redirect(reverse("edit_profile_page"))
        else:
            return redirect(reverse("login_page"))
