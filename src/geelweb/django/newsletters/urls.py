from django.conf.urls import url
from django.views.generic import TemplateView
from geelweb.django.newsletters import views

urlpatterns = [
    url(r'^subscribe/$', views.subscribe, name='newsletters_subscribe'),
    url(r'^thanks/$', TemplateView.as_view(template_name="newsletters/thanks.html"), name='newsletters_subscription_confirmed'),
]
