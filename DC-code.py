import tweepy
import pandas as pd

#api keys
api_key="******************************"
api_secret="************************************"
access_token="***************************************"
access_token_secret="*****************************"

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

