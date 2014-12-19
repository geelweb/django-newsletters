from django.db import models
from django.utils.translation import ugettext as _

class Newsletter(models.Model):
    email = models.EmailField(unique=True, error_messages={'unique': _('This email is already registered')})
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    optin = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('email')
        verbose_name_plural = _('emails')

    def __unicode__(self):
        return self.email
