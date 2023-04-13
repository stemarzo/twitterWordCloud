from wordcloud import WordCloud, get_single_color_func
from PIL import Image
import numpy as np
import pandas as pd

def createWordcloud(wordColor, backgroundColor, wordList, numero, max_words):
    wordList.index = [words.upper() for words in wordList.index]
    wordList.index = [words.replace(" ", "-") for words in wordList.index]
    mask = np.array(Image.open('/home/stefano/Desktop/WordCloud/number_image/' + numero + '.png'))
    col_func = get_single_color_func(wordColor)
    wordcloud = WordCloud(mode="RGB",
                      font_path="/home/stefano/Desktop/WordCloud/execution_file/Arial.ttf",
                      max_words = max_words,
                      min_font_size = 10,
                      mask=mask,
                      background_color= backgroundColor).generate_from_frequencies(wordList)
    return wordcloud.recolor(color_func=col_func)

def changeWord(wordList, path):
    changeList = pd.read_csv(path, names=['old', 'new'])
    for word in wordList.index:
        result = changeList.loc[changeList['old'].str.contains(word, case=False)]
        if len(result.index) > 0:
            print(changeList.loc[result.index[0], 'new'])
            wordList.rename(index={word : changeList.loc[result.index[0], 'new']},inplace=True)

    