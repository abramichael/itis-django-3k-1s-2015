from django.db import models

class RawUser(models.Model):
    
    username = models.CharField(
    	max_length=30,
    	#null=True
    	#default=...
    	unique=True,
    	#primary_key=True
    )
