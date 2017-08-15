from django.shortcuts import render, redirect, reverse
from django.conf import settings
from apps.twitter_app.models import Twitter

def index(request):
    twitter = Twitter()

    context = {
        'tweets': twitter.search('%23hillarysoqualified')
    }

    return render(request, 'twitter_app/index.html', context)