# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Here is webui_agent view.")

import os, subprocess, sys, time

def stamptime (request):
    # print repr (request.META)
    t = time.strftime ("%Y-%m-%d %H:%M:%S", time.gmtime ())
    subprocess.call ('echo %s >> /home/kraljo/tmp/1.txt' % t, shell=True)
    response = HttpResponse ("agnt: %s" % t)
    set_access_control_headers (response)
    print repr (response._headers)
    return response

def set_access_control_headers(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = 1000
    response['Access-Control-Allow-Headers'] = '*'
