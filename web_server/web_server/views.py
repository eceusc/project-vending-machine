from django.http import HttpResponse

def root(request):
    return HttpResponse('hiya')
