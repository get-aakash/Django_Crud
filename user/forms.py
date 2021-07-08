from django.db.models.fields import CharField
from .models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ["name", "email", "address", "password", "image"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter name",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Email",
                    "style": "width:36ch",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter Your Password",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:36ch",
                    "placeholder": "Enter Your address here",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        print(email)

        if not email.endswith("@cowhite.com"):
            raise forms.ValidationError("Domain of email is not valid")
        else:
            return email
