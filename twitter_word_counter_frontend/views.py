from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.express as px

import sys
sys.path.insert(0, 'twitterWordCounterApplication/twitter_word_counter.py')
from twitter_word_counter import most_common_word_from_user

def index(request):
    chart = {}
    if request.method == 'POST':
        words = most_common_word_from_user(request.POST['user_name'],int(request.POST['number_of_tweets']),int(request.POST['number_of_words']))
        if len(words) > 0:
            df = pd.DataFrame(list(map(list, zip(*words))))
            df = df.transpose()
            fig = px.bar(df, x=0, y=1)
            print(fig)
            bar = plot(fig, output_type="div")
            chart = { 'plot_div': bar }
            
    return render(request, "index.html", chart)
    