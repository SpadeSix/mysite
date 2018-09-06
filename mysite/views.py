#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse,Http404
from django.template import Context
# from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import render
import datetime


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def current_datetime(request):
    # now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',
                              {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def test1(request):
    return render_to_response('test1.html',
                              {"k":1,"v":"alex"})