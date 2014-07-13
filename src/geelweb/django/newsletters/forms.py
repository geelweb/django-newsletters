from django import forms
from geelweb.django.twitter_bootstrap_form.widgets import TextInputWithButton
from geelweb.django.newsletters.models import Newsletter

DEFAULT_ERRORS = {
    'required': u'You have to provide an email to register to our newsletter',
    'invalid': u'Please, provide a valid email address',
}

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        labels = {
            'email': u'Subscribe to our newsletter',
        }
        error_messages = {
            'email': DEFAULT_ERRORS,
        }
        widgets = {
            'email': TextInputWithButton(attrs={
                'placeholder': u'Enter your email address',
                'required':'required',
                'id': 'newsletter_email',
            }, btn_attrs={
                'type': 'button',
                'onclick': "newsletter.add('#newsletter_email');",
            }),
        }

    def clean_email(self):
        return self.cleaned_data['email'].lower()

