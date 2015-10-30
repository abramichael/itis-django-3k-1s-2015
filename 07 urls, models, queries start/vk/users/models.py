from django.db import models

class RawUser(models.Model):
    MALE = "M"
    FEMALE = "F"
    genders = (
        (MALE, "Male"), (FEMALE, "Female")
    )
    gender = models.CharField(max_length=1, choices=genders, default=FEMALE)
    year = models.PositiveSmallIntegerField(default=1995)
    friend = models.ManyToManyField('RawUser',
        symmetrical=True,
        #through=
        #related_name="friend_list" - if not symmetrical
        )
    username = models.CharField(
    	max_length=30,
    	#null=True
    	#default=...
    	unique=True,
    	#primary_key=True
    )

    def __unicode__(self):
        return self.username