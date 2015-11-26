from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

def validate_length(value):
    if len(value):
        raise ValidationError(u'To less info')


GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)


class Profile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER)
    about_me = models.TextField(blank=True, validators=[validate_length])
    hide_from_anon = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)




