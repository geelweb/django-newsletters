from django.contrib import admin
from geelweb.django.newsletters.models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'optin', 'date_created')
    list_filter = ('optin', )

admin.site.register(Newsletter, NewsletterAdmin)

