from django import template
from geelweb.django.newsletters.forms import NewsletterForm

register = template.Library()

@register.inclusion_tag('newsletters/form.html')
def newsletter_form(on_success=None):
    return {
        'form': NewsletterForm(),
        'on_success': on_success,
    }
