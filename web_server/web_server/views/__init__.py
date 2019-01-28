from django.http import HttpResponse
import os
def root(request):
    return HttpResponse('hiya' + os.getenv('password'))
