from django.db.models.fields import CharField
from .models import User
from django import forms
from django.forms import ValidationError


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
        valemail = self.cleaned_data["email"]
        if len(valemail) < 10:
            raise forms.ValidationError("The length of email should be more than 10")
        return valemail

    def clean_name(self):
        valname = self.cleaned_data["name"]
        if len(valname) < 4:
            raise forms.ValidationError("The name is too small")
        return valname
