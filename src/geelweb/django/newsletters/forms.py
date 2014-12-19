from django import forms
from django.utils.translation import ugettext as _

from geelweb.django.twitter_bootstrap_form.widgets import TextInputWithButton
from geelweb.django.newsletters.models import Newsletter

DEFAULT_ERRORS = {
    'required': _('You have to provide an email to register to our newsletter'),
    'invalid': _('Please, provide a valid email address'),
}

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        labels = {
            'email': _('Subscribe to our newsletter'),
        }
        error_messages = {
            'email': DEFAULT_ERRORS,
        }
        widgets = {
            'email': TextInputWithButton(attrs={
                'placeholder': _('Enter your email address'),
                'required':'required',
                'id': 'newsletter_email',
            }, btn_attrs={
                'type': 'button',
                'onclick': "newsletter.add('#newsletter_email');",
            }),
        }

    def clean_email(self):
        return self.cleaned_data['email'].lower()

