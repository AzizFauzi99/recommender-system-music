import numpy as np
import pandas as pd
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

df = pd.read_csv('dataset/songdata.csv')

# preprocessing
df = df.sample(n=20000, random_state=42).drop('link', axis=1).reset_index(drop=True)
# hapus \n dalam lirik
df['text'] = df['text'].str.replace(r'\n', '')
# case folding
df['text'] = df['text'].str.lower()
# stemming bahasa inggris
porter = PorterStemmer()
df['text'] = df['text'].apply(lambda x: ' '.join([porter.stem(word) for word in x.split()]))
# stopword removal
stop = stopwords.words('english')
df['text'] = df['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

# TF-IDF
tfidf = TfidfVectorizer(analyzer='word')
lyrics_matrix = tfidf.fit_transform(df['text'])
# cosine similarity
cosine_similarities = cosine_similarity(lyrics_matrix) 

similarities = {}

for i in range(len(cosine_similarities)):
    # Sekarang kita akan mengurutkan setiap elemen dalam cosine_similarities dan mendapatkan indeks lagu-lagu tersebut
    similar_indices = cosine_similarities[i].argsort()[:-10:-1] 
    # Setelah itu, kita akan menyimpan dalam similarities setiap nama dari 10 lagu yang paling mirip
    # Kecuali yang pertama yang merupakan lagu yang sama
    similarities[df['song'].iloc[i]] = [(cosine_similarities[i][x], df['song'][x], df['artist'][x]) for x in similar_indices][1:]

class ContentBasedRecommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    # print top 5 lagu yang direkomendasikan
    def _print_message(self, song, recom_song):
        jml_item = len(recom_song)
        
        print(f"Anda sedang memutar lagu \"{song}\"")
        print(f'{jml_item} rekomendasi lainnya yang mungkin anda sukai:')
        for i in range(jml_item):
            print(f"No.{i+1}:")
            print(f"\"{recom_song[i][1]}\" dari \"{recom_song[i][2]}\" => dengan {round(recom_song[i][0], 3)} similarity score") 
            print("--------------------")
        
    def recommend(self, target_song):
        song = target_song
        recom_song = self.matrix_similar[song][:5]
        self._print_message(song=song, recom_song=recom_song)

recommedations = ContentBasedRecommender(similarities)
recommedations.recommend("Christmas Is Dead")