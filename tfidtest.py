import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')

df1=pd.read_csv('./dataset/tmdb_5000_credits.csv')
df2=pd.read_csv('./dataset/tmdb_5000_movies.csv')

df1.columns = ['id','title','cast','crew']
df2= df2.merge(df1,on='id')
