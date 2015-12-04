from django import forms
from django.core.validators import RegexValidator
from profiles.models import Profile


class LoginForm(forms.Form):
    login = forms.CharField(label="USERNAME")
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(validators=[RegexValidator(
        r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", "Wrong format!!!"
    )])

    class Meta:
        model = Profile
        #fields = ["gender", "about_me", "hide_from_anon", "phone_number"]
        exclude = ["user"]