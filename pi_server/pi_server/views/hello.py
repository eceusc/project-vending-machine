from django.http import HttpResponse, HttpResponseBadRequest

def hello(request):
    return HttpResponse('Good job, your pi server is working!')
