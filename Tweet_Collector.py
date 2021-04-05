#getting started 
import tweepy as tw
import pandas as pd
import os

#insert keys and secret tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret= ""

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#disneyplus"
date_since = "2021-01-01"

#fetching tweets

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(100)

#filtering retweets
new_search = search_words + " -filter:retweets"
new_search

list_tweets = [tweet.text for tweet in tweets]

#print(list_tweets)

tweets = tw.Cursor(api.search, 
                           q=new_search,
                           lang="en",
                           since=date_since).items(100)
users_locs = [[tweet.user.screen_name, tweet.user.location,tweet.text] for tweet in tweets]

# Dataframe -test
tweet_df = pd.DataFrame(data=users_locs, 
                    columns=['user', "location","tweet"])
print(tweet_df)

#creating sample tweets to check connection
#will make an object later that gives dataframe to the other file
tweet_df.to_csv('sample_tweets.csv')



