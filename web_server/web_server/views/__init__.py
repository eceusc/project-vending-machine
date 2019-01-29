from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from web_server.views.handle_github_event import handle_github_event

def root(request):
    return HttpResponse('Good job, your server is working!')

@csrf_exempt
def github_webhook(request):
    
    if request.method != 'POST':
        return HttpResponseBadRequest('needs to be post \U0001F61E')

    return handle_github_event(request)
