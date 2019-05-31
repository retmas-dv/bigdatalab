from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from siteapp import views
import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.default),
    url(r'^pages/.+/$', views.pages_handler)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
