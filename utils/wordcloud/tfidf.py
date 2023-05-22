from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 

def tfIdfList(tweets_df):
    tv = TfidfVectorizer(use_idf=True, ngram_range=(1,3))
    tv.fit(tweets_df['text'].astype(str))
    tweets_tfidf = tv.transform(tweets_df['text'].astype(str))
    feature_names = tv.get_feature_names_out()
    dense = tweets_tfidf.todense()
    lst1 = dense.tolist()
    df = pd.DataFrame(lst1, columns=feature_names)
    return df.T.sum(axis=1)

def tfIdfScore(tweets_df, lunghezza):
    scoreList = tfIdfList(tweets_df).sort_values(ascending=False)[: int(lunghezza+ (0.1*lunghezza))]
    return scoreList


def removeWordScoreList(scoreList, path):
    stop_word = []
    with open(path) as f:
        stop_word = f.read().splitlines()
    for parola in stop_word:
        try:
            scoreList = scoreList.drop(parola)
            print(parola)
        except:
            print("no word")
    return scoreList
