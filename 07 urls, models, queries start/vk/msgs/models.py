from django.db import models

from users.models import RawUser

from datetime import datetime

# Create your models here.
class Msg(models.Model):
    sender = models.ForeignKey(RawUser, related_name="msgs_sent")
    recipient = models.ForeignKey(RawUser, related_name="msgs_received")
    date = models.DateTimeField(default=datetime.now())
    text = models.TextField()
