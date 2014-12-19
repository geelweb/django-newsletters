from django import template
from geelweb.django.newsletters.forms import NewsletterForm

register = template.Library()

@register.inclusion_tag('newsletters/form.html')
def newsletter_form(*args, **kwargs):
    on_success = kwargs['on_success'] if 'on_success' in kwargs else None

    form = NewsletterForm()
    if 'label' in kwargs:
        form.fields['email'].label = kwargs['label']

    return {
        'form': form,
        'on_success': on_success,
    }
