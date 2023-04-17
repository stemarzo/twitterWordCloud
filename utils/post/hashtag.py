import pandas as pd
from re import sub

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

def getHashTag(wordRank):
    lista = pd.DataFrame(wordRank[:30]).index
    lista = ["#"+ camel_case(word) for word in lista]
    ' '.join(lista)
    return lista
