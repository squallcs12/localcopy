from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import defaults
from django.http.response import Http404
from django.views.static import serve
from django.core import management


def index(request, path):
    host = request.META['HTTP_HOST']
    return HttpResponseRedirect("/media2/{host}/{path}".format(host=host, path=path))


def static(request, *args, **kwargs):
    try:
        response = serve(request, *args, **kwargs)
    except Http404:
        management.call_command('disable')
        url = "http://{path}".format(path=kwargs['path'])
        management.call_command('copy', url)
        print("Copied {url}".format(url=url))
        management.call_command('enable')
        raise
    else:
        return response