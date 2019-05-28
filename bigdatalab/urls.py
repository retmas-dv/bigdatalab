from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'siteapp.views.default'),
    url(r'^pages/.+/$', 'siteapp.views.pages_handler')
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
