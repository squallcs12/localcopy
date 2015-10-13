from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from localcopy.views import static

urlpatterns = [
    url(r'^media2/(?P<path>.*)$', static, {'document_root': settings.MEDIA_ROOT,}),
    url('^(.*)$', 'localcopy.views.index')
]
