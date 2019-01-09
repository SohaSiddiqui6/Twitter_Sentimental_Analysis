from textblob import TextBlob
import nltk
import tweepy

customer_key =''
customer_secret =''
access_token =''
access_secret_token =''

auth = tweepy.OAuthHandler(customer_key,customer_secret)
auth.set_access_token(access_token,access_secret_token)
api = tweepy.API(auth)
public_tweets =api.search('Zuckerburg')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
