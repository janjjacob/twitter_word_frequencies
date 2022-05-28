from django.http import HttpResponse
from django.shortcuts import render

import sys
sys.path.insert(0, 'twitterWordCounterApplication/twitter_word_counter.py')
from twitter_word_counter import most_common_word_from_user

def index(request):
    words = {}
    if request.method == 'POST':
        words = { 'words': most_common_word_from_user(request.POST['user_name'],int(request.POST['number_of_tweets']),int(request.POST['number_of_words'])) }
    return render(request, "index.html", words)
    