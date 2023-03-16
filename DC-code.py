import tweepy
import pandas as pd

#api keys
api_key="J4yP3oGhSk52shiaBJpzrcYW2"
api_secret="N2z70hbM4osq0EN0eZjN9KxSyPrvhhb2tKwknda2JljjQkIlkH"
access_token="1004955501698928640-9j3dYmFEueS4nMO9eA1u7dzOO2wcIy"
access_token_secret="pwxhH0kLEAs1EHTqRthkpf00J3UJJsHB6NNy6XwJzMTYd"

# Authenticate to Twitter
auth=tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#number of tweets 
tweetNo=600
tweets=[]
time=[]

#keyword search
for i in tweepy.Cursor(api.search_tweets,q="@",tweet_mode="extended").items(tweetNo):
    tweets.append(i.full_text)
    time.append(i.created_at)
    
#create DataFrame    
df=pd.DataFrame({'Tweets':tweets})

print(df)


#save tweets into excle file
df.to_excel('A.xlsx')

