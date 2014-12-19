from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _

from geelweb.django.newsletters.forms import NewsletterForm

import json

def subscribe(request):
    form = NewsletterForm(request.GET or None)
    if form.is_valid():
        form.save()

        if request.is_ajax():
            return HttpResponse(json.dumps({
                    'code': 200,
                    'message': _('Thanks, we registered your subscription'),
                }),  content_type='application/json')

        redirect_to = request.POST.get(
                'on_success',
                request.GET.get('on_success', reverse('newsletters_subscription_confirmed')))
        return HttpResponseRedirect(redirect_to)

    if request.is_ajax():
        return HttpResponse(json.dumps({
                'code': 500,
                'message': form.errors['email'],
            }), content_type='application/json')

    return render_to_response('newsletters/form.html', {
        'form': form,
        }, context_instance=RequestContext(request))

