import nltk
nltk.download('punkt')
nltk.download('stopwords')
import treetaggerwrapper
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import re

def tweetsTokenize(tweets_df):
    tweets_df['text'] = tweets_df['text'].apply(word_tokenize)
    return tweets_df


def tweetsLemmatization(tweets_df):
    tweets_df['text'] = tweets_df['text'].apply(lemmaSentence)
    return tweets_df

def lemmaSentence(token_words):
    tagger = treetaggerwrapper.TreeTagger(TAGLANG='it', TAGDIR='treetagger/')
    lemma_text=[]
    for word in token_words:
      tag = treetaggerwrapper.make_tags(tagger.tag_text(word),
                                   allow_extra = True)[0]
      lemmeOption2=tag[2].split("|")
      args=lemmeOption2[0]
      if args == '@card@': args = tag.word
      lemma_text.append(args)
    return lemma_text
  
def stopWordRemoval(text, stopwords_list):
  return ([word for word in text if word not in stopwords_list])

def stopWordRemoval2(text, stopwords_list):
  text = " ".join(text)
  for word in stopwords_list:
    text = re.sub(r"\b%s\b" % word, '', text)
  return word_tokenize(text)

def stopWordRemovalDF(tweets_df):
    englishStopwords = stopwords.words('english')
    italianStopwords = stopwords.words('italian')
    stop_word = []
    with open('./execution_file/stop_word.txt') as f:
      stop_word = f.read().splitlines()
    tweets_df['text'] = tweets_df['text'].apply(lambda x: stopWordRemoval(x, englishStopwords))
    tweets_df['text'] = tweets_df['text'].apply(lambda x: stopWordRemoval(x, italianStopwords))
    tweets_df['text'] = tweets_df['text'].apply(lambda x: stopWordRemoval2(x, stop_word))
    return tweets_df

def tweetsManipulation(tweets_df):
   tweets_df = tweetsTokenize(tweets_df)
   tweets_df = tweetsLemmatization(tweets_df)
   #tweets_df = stopWordRemovalDF(tweets_df)
   return tweets_df

def saveTweet(tweets, path):
   pd.DataFrame(tweets).to_csv(path, index=False)