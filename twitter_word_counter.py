import tweepy
from tweepy import OAuthHandler
from collections import Counter
from nltk.corpus import stopwords

consumer_key = 'kFLxVcDQMtKyOj2Mp8zZyKeWQ'
consumer_secret = 'heHnWFaPKYm04ybplcojEls9iUszXT0XRtp8gBUXKKRu4bjZI2'
access_token = '872400637883027457-Kh5BxMPBJ0YTGHgPnPZC1XLtCj7GxbK'
access_secret = 'xwRLDBXVapKPsZ7k5FqpikH44pI0DZgBjfkLYp0l30xps'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def getRecentTweetsFromUser(user, count):
    return api.user_timeline(screen_name=user, include_rts=False, count=count)

def getTweetsSinceDateFromUser(user, date):
    return tweepy.Cursor(api.search_full_archive,query='from:@'+user+' -filter:retweets',label='fullarchive',fromDate=date)

def most_common_word_from_user(user, number_of_tweets, number_of_words):
    tweets = getRecentTweetsFromUser(user, number_of_tweets)
    count_all = Counter()
    for status in tweets:
        tweet_words = status.text.split(' ')
        for word in tweet_words:
            if len(word) != 0 and word not in stopwords.words('english'):
                if word[0] != '@':
                    count_all.update([word.lower()])
    return count_all.most_common(number_of_words)
    
def mostCommonWordsFromUserFromDate(user, date):
    tweets = getTweetsSinceDateFromUser(user, date)
    count_all = Counter()
    tweets_list = [tweets.text for tweet in tweets.items()]
    for tweet in tweets.items():
        print(tweet.text)
    for tweet in tweets_list:
        print(tweet.text)
        tweet_words = tweet.text.split(' ')
        for word in tweet_words:
            if len(word) != 0 and word not in stopwords.words('english'):
                if word[0] != '@':
                    count_all.update([word.lower()])
    print(count_all.most_common(10))