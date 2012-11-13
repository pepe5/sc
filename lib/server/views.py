# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


import time
from django.views.decorators.http import condition

@condition(etag_func=None)
def stream_response(request):
    #(<) print repr (request)
    resp = HttpResponse( stream_response_generator (request), mimetype='text/html')
    return resp

def stream_response_generator (request):
    yield "<html><body>\n"
    for x in range(1,11):
        yield "<div>%s</div>\n" % x
        yield " " * 1024  # Encourage browser to render incrementally
        time.sleep(1)
    yield "</body></html>\n"


import os, subprocess, sys

@condition(etag_func=None)
def stream_tail(request):
    print 'stream_tail: PATH_INFO: ' + (request.META['PATH_INFO'][12:])
    resp = HttpResponse (stream_tail_generator (request), mimetype='text/html')
    return resp

def stream_tail_generator (request):
    yield "<html><body>\n"
    yield ''' <a href="#0"
	onclick="javascript:xmlHttp=new XMLHttpRequest();
        xmlHttp.open("GET", "http://localhost:8009/stamp", false);
        xmlHttp.send(null);
        return false;">
        [stamp it!] </a>
        '''
    process = subprocess.Popen(['inotail','-f', '/home/kraljo/tmp/1.txt'], bufsize=1, stdout=subprocess.PIPE)
    while 1:
        ln = process.stdout.readline ()
        print "srv: %s" % ln,
        yield ('<br> %s' % ln) + (" " * 1024)
    yield "</body></html>\n"
