import pandas as pd
from datetime import date, timedelta
import tweepy

OGGI = date.today() - timedelta(days=0)
IERI = OGGI - timedelta(days=1)
OGGI = OGGI.strftime('%Y-%m-%d')
IERI = IERI.strftime('%Y-%m-%d')

ID_PROFILI = [395218906]
bearer_token = "AAAAAAAAAAAAAAAAAAAAAB4SbQEAAAAAq2Oa7eu7zbrg2E4B3xLIURWwDBk%3DXxO5cyKNFlrd9LSxYoP1weQmGep38pJoIyH9AG4Pzom0BKqZWX"
df = pd.DataFrame(columns=['text', 'impression'])

client = tweepy.Client(bearer_token)
response = client.get_users_tweets(395218906, tweet_fields="public_metrics", start_time=IERI+"T06:00:00Z", 
                                     end_time=OGGI+"T06:00:00Z", max_results=100)

for tweet in response.data:
    if ('RT @' not in tweet.text):
       df = pd.concat([df,pd.DataFrame.from_dict({'text': [tweet.text], 'impression':[tweet['public_metrics']['impression_count']]})])

df=df.reset_index()


print(df.sort_values(by=['impression'], ascending=False))
