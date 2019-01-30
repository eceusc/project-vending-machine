from web_server.views.gh_hash import hash
from django.http import HttpResponse, HttpResponseBadRequest
import json
import os

webhook_secret_base = os.getenv('GITHUB_WEBHOOK_SECRET') # TODO remove

def is_legit(request):
    webhook_secret = hash(webhook_secret_base, request)
    given_secret = request.META.get('HTTP_X_HUB_SIGNATURE')
    # TODO: check if given_secret and webhook_secret is same
    return True

def handle_github_event(request):
    if not is_legit(request):
        return HttpResponseBadRequest('bad secret, {}!'.format(given_secret))

    payload = request.POST
    print('received this payload:')
    print(payload)
    print("Test worked")
    
    from github import Github
    g = Github(os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"))
    repo = g.get_repo("chrisjrobles/project-vending-machine")
    payloadJson = json.loads(payload.get("payload"))
    id = payloadJson.get("issue").get("number")
    issue = repo.get_issue(id)
    issue.create_comment('Thanks for reporting an issue!')
    
    # GOAL
    # When an issue is opened, comment on issue, say they got 50 tokens
    # when an issue is closed, comment on issue, say thanks, 50 tokens

    return HttpResponse('\U0001F44D')
