from django.db import models
from django.contrib.auth.models import User

def validate_grade(value):
    if value < 0:
        raise ValidationError(u'Grade must be greater than 0')

GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)

class Profile(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1, choices=GENDER)
    about_me = models.TextField(blank=True)




