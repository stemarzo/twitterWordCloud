import re
import pandas as pd

def dropDuplicates(tweets_df):
    tweets_df = tweets_df.drop_duplicates('text',keep='first')
    return tweets_df

def toLower(phrase):
  phrase = phrase.lower()
  return phrase

def removeEmoji(phrase):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', phrase)

def removeUrls(sentence):
    http_pattern = re.compile(r"http\S+") 
    cleaned_sentence = re.sub(http_pattern,'',sentence).strip()
    www_pattern = re.compile(r"www\S+") 
    cleaned_sentence = re.sub(www_pattern,'',cleaned_sentence)
    return cleaned_sentence

def removeSpecialCharactersPunctuations(sentence):
    pattern = re.compile("[^a-zA-Z0-9]+") 
    cleaned_text  = re.sub(pattern,' ',sentence).strip()
    return cleaned_text

def tweetsCleaning(tweets_df):
  tweets_df = dropDuplicates(tweets_df)
  tweets_df['text'] = tweets_df['text'].apply(toLower)
  tweets_df['text'] = tweets_df['text'].apply(removeEmoji)
  tweets_df['text'] = tweets_df['text'].apply(removeUrls)
  tweets_df['text'] = tweets_df['text'].apply(removeSpecialCharactersPunctuations)
  tweets_df['text'] = tweets_df['text'].apply(toLower) 
  return tweets_df
