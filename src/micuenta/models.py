from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    apellido = models.CharField(null=False, blank=True, max_length=50)
    rut = models.CharField(null=False, blank=True, max_length=50)
    telefono = models.CharField(null=False, blank=True, max_length=50)

    website = models.URLField(blank=True)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return smart_unicode(self.user.email)