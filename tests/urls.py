from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^newsletter/', include('geelweb.django.newsletters.urls'))
)

