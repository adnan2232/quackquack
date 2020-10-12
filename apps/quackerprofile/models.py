from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField, OneToOneField

class QuackerProfile(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE)
    follows = ManyToManyField('self',related_name='followed_by',symmetrical=False)
    avatar = models.ImageField(upload_to="upload/",blank=True,null=True)

User.quackerprofile = property(lambda u: QuackerProfile.objects.get_or_create(user=u)[0])