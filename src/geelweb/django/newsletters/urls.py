from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('geelweb.django.newsletters.views',
    url(r'^subscribe/$', 'subscribe', name='newsletters_subscribe'),
)

urlpatterns = urlpatterns + patterns('',
    url(r'^thanks/$', TemplateView.as_view(template_name="newsletters/thanks.html"), name='newsletters_subscription_confirmed'),
)
