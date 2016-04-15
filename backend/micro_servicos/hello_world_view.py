from django.http.response import HttpResponse


def index(request):
    print request
    return HttpResponse("Hello world from django")
