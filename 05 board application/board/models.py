from django.db import models

# Create your models here.
class Post(models.Model):
	txt = models.CharField(max_length=150)
	published_at = models.DateTimeField()

	def __unicode__(self):
		return self.txt[:10]