from urllib.parse import uses_fragment
import tweepy
from tweepy import OAuthHandler
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

consumer_key = 'kFLxVcDQMtKyOj2Mp8zZyKeWQ'
consumer_secret = 'heHnWFaPKYm04ybplcojEls9iUszXT0XRtp8gBUXKKRu4bjZI2'
access_token = '872400637883027457-Kh5BxMPBJ0YTGHgPnPZC1XLtCj7GxbK'
access_secret = 'xwRLDBXVapKPsZ7k5FqpikH44pI0DZgBjfkLYp0l30xps'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getRecentTweetsFromUser(user, count):
    return api.user_timeline(screen_name=user, include_rts=False, count=count)

# def getTweetsSinceDateFromUser(user, date):
#     return tweepy.Cursor(api.search_full_archive,query='from:@'+user+' -filter:retweets',label='fullarchive',fromDate=date)

def mostCommonWordsFromUser(user, count):
    tweets = getRecentTweetsFromUser(user, count)
    count_all = Counter()
    for status in tweets:
        # print(status.text)
        tweet_words = status.text.split(' ')
        for word in tweet_words:
            if len(word) is not 0:
                if word[0] is not '@':
                    count_all.update([word.lower()])
    return count_all.most_common(10)
    
# def mostCommonWordsFromUserFromDate(user, date):
#     tweets = getTweetsSinceDateFromUser(user, date)
#     count_all = Counter()
#     tweets_list = [tweets.text for tweet in tweets.items()]
#     for tweet in tweets.items():
#         print(tweet.text)
#     for tweet in tweets_list:
#         print(tweet.text)
#         tweet_words = tweet.text.split(' ')
#         for word in tweet_words:
#             if len(word) is not 0:
#                 if word[0] is not '@':
#                     count_all.update([word.lower()])
#     print(count_all.most_common(10))
        
# user = input('choose a username ')
# count = input('choose a count ')

# common_words_from_user = mostCommonWordsFromUser(user,count)

# labels, y = zip(*common_words_from_user)
# x = np.arange(len(labels)) 
# width = 1

# plt.bar(x, y, width, align='center')

# plt.xticks(x, labels)
# plt.yticks(y)
# plt.xticks(rotation=90)
# plt.show()