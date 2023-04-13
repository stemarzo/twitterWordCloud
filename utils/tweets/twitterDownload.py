import tweepy
import pandas as pd

def getTweetsAccount(accountId, startPeriod, endPeriod, client):
  response = client.get_users_tweets(accountId, start_time=startPeriod, 
                                     end_time=endPeriod, max_results=100)
  tweets = []
  try:
    for tweet in response.data:
      if ('RT @' not in tweet.text):
        tweets.append(tweet.text)
  except:
    print("No Tweets")
  return tweets

def getAllTweetsAccount(accountId, yesterday, today, client):
  startTime = [yesterday+"T06:00:00Z",yesterday+"T12:00:00Z",yesterday+"T18:00:00Z", 
            today+"T00:00:00Z"]
  endTime = [yesterday+"T12:00:00Z",yesterday+"T18:00:00Z",yesterday+"T23:59:59Z", 
          today+"T06:00:00Z"]
  tweets = []
  for i in range(len(startTime)):
    tweets.extend(getTweetsAccount(accountId, startTime[i], endTime[i], client))
  return tweets

def getAllTweets(accountIds, yesterday, today, twitterToken):
  client = tweepy.Client(twitterToken)
  tweets = []
  for accountId in accountIds:
    tweets.extend(getAllTweetsAccount(accountId, yesterday, today, client))
  tweetsDf = pd.DataFrame (tweets, columns = ['text'])
  return tweetsDf