# -*- coding: utf-8 -*-


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

# Information about extending auth.User:
# https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users
class FVISUser(models.Model):
     '''
     Extended User registry.
     
     In order to use this model to be a project profile, this app
     should be installed and the appropiate setting should be set:
     
         AUTH_PROFILE_MODULE = 'fvisusers.FVISUser'
     
     Information about extending auth.User:
     https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users
     '''

     user = models.OneToOneField(User)
     phone = models.CharField(verbose_name=u'teléfono', max_length=100, blank=True)
     ci = models.IntegerField(verbose_name=u'cédula de identidad', null=False)
     
     def __unicode__(self):
          return u'{0} {1} <{2}>'.format(self.user.first_name, self.user.last_name, self.user.username)
     
# As the auth doc says:
#
#"... You need to register a handler for the signal
# django.db.models.signals.post_save on the User model, and, in the
# handler, if created=True, create the associated user profile."
def create_fvis_user(sender, instance, created, **kwargs):
     if created:
          FVISUser.objects.create(
               user=instance,
               ci=kwargs.get('ci', 0),
               phone=kwargs.get('phone', ''))
               
post_save.connect(create_fvis_user, sender=User)
