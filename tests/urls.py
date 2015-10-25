from django.conf.urls import url, include

urlpatterns = [
    url(r'^newsletter/', include('geelweb.django.newsletters.urls'))
]

