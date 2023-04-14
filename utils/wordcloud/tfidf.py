from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 

def tfIdfList(tweets_df):
    tv = TfidfVectorizer(use_idf=True, ngram_range=(1,2))
    tv.fit(tweets_df['text'].astype(str))
    tweets_tfidf = tv.transform(tweets_df['text'].astype(str))
    feature_names = tv.get_feature_names_out()
    dense = tweets_tfidf.todense()
    lst1 = dense.tolist()
    df = pd.DataFrame(lst1, columns=feature_names)
    return df.T.sum(axis=1)

def tfIdfScore(tweets_df, lunghezza):
    scoreList = tfIdfList(tweets_df).sort_values(ascending=False)[: int(lunghezza+ (0.1*lunghezza))]
    for parola in scoreList.index:
        matching = [s for s in scoreList.index if parola in s]
        if len(matching) > 1:
            print(parola)
            scoreList = scoreList.drop(parola)
    return scoreList


