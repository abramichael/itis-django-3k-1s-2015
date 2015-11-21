from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    class Meta:
        db_table = "tweets"

    user = models.ForeignKey(User)
    txt = models.CharField(max_length=140)
    pub_date = models.DateTimeField()