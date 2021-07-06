from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import (
    force_bytes,
    force_str,
    force_text,
    DjangoUnicodeDecodeError,
)
from .utils import generate_token
from django.conf import settings
from django.core.mail import EmailMessage

from django.shortcuts import redirect, render


from .forms import LoginForm, RegisterForm, User

# Create your views here.


def send_activation_email(user, request):

    current_site = get_current_site(request)
    email_subject = "Activate Your Account"
    email_body = render_to_string(
        "activation.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.id)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email],
    )
    email.send()


def login_user(request):
    if request.user.is_authenticated:
        print("authenticated")
        return HttpResponseRedirect("user/userread")

    if request.method == "POST":
        fm = LoginForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data.get("email")
            password = fm.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            print(user)
            if not user.is_email_verified:
                messages.add_message(request, messages.ERROR, "Email is not verifed")
                return HttpResponseRedirect("/")
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("user/userread")
    fm = LoginForm()
    return render(request, "login.html", {"form": fm})


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form):
        request = self.request
        current_user = request.user
        print(current_user)
        if request.user.is_authenticated:
            print("authenticated")
            return HttpResponseRedirect("user/userread")
        else:
            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=email, password=password)
                print(user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("user/userread")


def register(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        user = form.save()
        print(user.id)
        send_activation_email(user, request)
        print("the control is here")
        return HttpResponseRedirect("/")
    return render(request, "register.html", context)


def logout_user(request):
    logout(request)
    print("this is the logout")
    return HttpResponseRedirect("/")


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, "Email Verified")
        return redirect("/")
    return render(request, "activation-failed.html", {"user": user})
