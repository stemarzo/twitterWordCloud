import tweepy
import pandas as pd

def getTweetsAccount(accountId, startPeriod, endPeriod, client):
  response = client.get_users_tweets(accountId, tweet_fields="public_metrics", start_time=startPeriod, 
                                     end_time=endPeriod, max_results=100)
  tweets = []
  standing = pd.DataFrame(columns=['text', 'impression'])
  try:
    for tweet in response.data:
      if ('RT @' not in tweet.text):
        tweets.append(tweet.text)
        standing = pd.concat([standing,pd.DataFrame.from_dict({'text': [tweet.text], 'impression':[tweet['public_metrics']['impression_count']]})])
  except:
    print("No Tweets")
  
  return tweets, standing

def getAllTweetsAccount(accountId, yesterday, today, client):
  startTime = [yesterday+"T06:00:00Z",yesterday+"T12:00:00Z",yesterday+"T18:00:00Z", 
            today+"T00:00:00Z"]
  endTime = [yesterday+"T12:00:00Z",yesterday+"T18:00:00Z",yesterday+"T23:59:59Z", 
          today+"T06:00:00Z"]
  tweets = []
  for i in range(len(startTime)):
    first, second = getTweetsAccount(accountId, startTime[i], endTime[i], client)
    tweets.extend(first)
  return tweets

def getAllTweets(accountIds, yesterday, today, twitterToken):
  client = tweepy.Client(twitterToken)
  tweets = []
  for accountId in accountIds:
    tweets.extend(getAllTweetsAccount(accountId, yesterday, today, client))
  tweetsDf = pd.DataFrame (tweets, columns = ['text'])
  return tweetsDf

def getTweetsStanding(accountId, yesterday, today, twitterToken):
  client = tweepy.Client(twitterToken)
  first, standing = getTweetsAccount(accountId, yesterday, today, client)
  standing=standing.reset_index()
  standing=standing.sort_values(by=['impression'], ascending=False)
  return standing
