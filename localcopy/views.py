import os

from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import defaults
from django.http.response import Http404
from django.views.static import serve
from django.core import management
from django.conf import settings

from localcopy.utils import translate_path


def index(request, path):
    host = request.META['HTTP_HOST']
    query = request.META['QUERY_STRING']
    path = translate_path(path, query)
    raw_path = os.path.join(settings.BASE_DIR, path)

    if not os.path.isfile(raw_path):
        management.call_command('disable')
        try:
            url = "http://%s/%s?%s" % (host, path, query)
            management.call_command('copy', url)
            print("Copiedddddddddd %" % url)
        finally:
            management.call_command('enable')

    return HttpResponseRedirect("/media2/%s/%s" % (host, path))


def static(request, *args, **kwargs):
    response = serve(request, *args, **kwargs)
    response['Access-Control-Allow-Origin'] = '*'
    return response