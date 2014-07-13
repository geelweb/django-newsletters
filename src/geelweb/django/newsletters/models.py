from django.db import models

class Newsletter(models.Model):
    email = models.EmailField(unique=True, error_messages={'unique': u'This email is already registered'})
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    optin = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'

    def __unicode__(self):
        return self.email
