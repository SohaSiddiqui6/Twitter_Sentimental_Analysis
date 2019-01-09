from textblob import TextBlob
import nltk
import tweepy

customer_key ='29uCsjl30Xj5F1tzXHfFewyd3'
customer_secret ='EWYpPs572o56g21G1Hg4BKUjPrFK4qszUAdyac9xHSt5R16In0'
access_token ='844914942306406402-Z0CkDsbAzLdproyFG3vVCMaBxhhiOR0'
access_secret_token ='phHoqaynJZuHt8fsMlykbMO8nendE1HAK35Bgy4ThV9zn'

auth = tweepy.OAuthHandler(customer_key,customer_secret)
auth.set_access_token(access_token,access_secret_token)
api = tweepy.API(auth)
public_tweets =api.search('Zuckerburg')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
