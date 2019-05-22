import tweepy
from tweepy import OAuthHandler
import json
import datetime
import pickle
import time

start = time.time()

with open('team.pkl', 'rb') as f:
    team = pickle.load(f)
with open('record_list.pkl', 'rb') as f:
    record = pickle.load(f)
key1=record[0]
key2=record[1]
idid=record[2]
print(team[key1][0],key1, key2, idid)
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

if key2 ==1:
    username = team[key1][1]
    startDate = datetime.datetime(2018, 10, 17, 0, 0, 0)
    endDate =   datetime.datetime(2019, 5, 23, 0, 0, 0)
    
    tweets = []
    tmpTweets = api.user_timeline(username, count=200)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet._json)
    
    limit_count = 1        
    while (tmpTweets[-1].created_at > startDate and limit_count<16):
        print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
        tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id, count=200)
        limit_count += 1 
        if tmpTweets[0].created_at < endDate and tmpTweets[-1].created_at > startDate:
            for tweet in tmpTweets:
                tweets.append(tweet._json)
        else:
            for tweet in tmpTweets:
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    tweets.append(tweet._json)
    
    with open(team[key1][0]+'_1.pkl', 'wb') as f:
        pickle.dump(tweets, f)   
    key1 = key1+1    
    key2 = 1
    #current_id = tweets[-1]['id']
    current_id = 0

else:
    username = team[key1][1]
    startDate = datetime.datetime(2018, 10, 17, 0, 0, 0)
    endDate =   datetime.datetime(2019, 1, 25, 0, 0, 0)
    
    tweets = []
    tmpTweets = api.user_timeline(username, count=200, max_id = idid)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet._json)
    
    limit_count = 1        
    while (tmpTweets[-1].created_at > startDate and limit_count<16):
        print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
        tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id, count=200)
        limit_count += 1 
        if tmpTweets[0].created_at < endDate and tmpTweets[-1].created_at > startDate:
            for tweet in tmpTweets:
                tweets.append(tweet._json)
        else:
            for tweet in tmpTweets:
                if tweet.created_at < endDate and tweet.created_at > startDate:
                    tweets.append(tweet._json)
    
    with open(team[key1][0]+'_2.pkl', 'wb') as f:
        pickle.dump(tweets, f)
    key1+=1
    key2 = 1
    current_id = 0



record_list=[]
record_list.append(key1) #0~28
record_list.append(key2) #1、2
record_list.append(current_id)
with open('record_list.pkl', 'wb') as f:
    pickle.dump(record_list, f)

print(record_list)

end = time.time()
print(end - start)