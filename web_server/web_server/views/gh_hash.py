import hmac
from hashlib import sha1
from django.utils.encoding import force_bytes

def hash(wh, request):
    mac = hmac.new(force_bytes(wh), msg=force_bytes(request.body), digestmod=sha1)
    return 'sha1={}'.format(mac.hexdigest())
