# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Here is webui_agent view.")

import os, subprocess, sys, time

def stamptime (request):
    t = time.strftime ("%Y-%m-%d %H:%M:%S", time.gmtime ())
    subprocess.call ('echo %s >> /home/kraljo/tmp/1.txt' % t, shell=True)
    return HttpResponse ("agnt: %s" % t)
