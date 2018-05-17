from django.http import HttpResponse


def index(request):
    motd = "Hello! Nice to see you start learning Django!"
    return HttpResponse(motd)


