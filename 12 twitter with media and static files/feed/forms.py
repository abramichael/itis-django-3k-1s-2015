from django import forms
from django.forms import Textarea
from feed.models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["txt"]
        widgets = {
            "txt": Textarea()
        }

from django.forms.models import modelform_factory
TweetForm2 = modelform_factory(Tweet, fields=["txt"])