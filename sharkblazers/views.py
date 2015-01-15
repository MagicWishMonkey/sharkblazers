from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from sharkblazers import util

@csrf_exempt
def home(request):
    return HttpResponse("<html><body><h1>Hello.</h1></body></html>", content_type="text/html")