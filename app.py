import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests

def poster(imdb):
    response=requests.get('https://www.omdbapi.com/?apikey=5db06ee&i={}&plot=full'.format(imdb))
    data=response.json()

    return data['Poster']

def pred(movie):
    movie_index=df[df['title']==movie].index[0]
    similar=similarity[movie_index]
    movie_names=sorted(list(enumerate(similar)),reverse=True,key=lambda x:x[1])[:6]
    
    movie_list=[]
    imdb_list=[]
    for i in movie_names:
        movie_list.append(df.iloc[i[0]]['title'])
        imdb=df.iloc[i[0]]['imdb_id']
        imdb_list.append(poster(imdb))
    return movie_list,imdb_list

df=pickle.load(open('D:/projects/bollywood_movies/bollywood_movies.pkl','rb'))
similarity=pickle.load(open('D:/projects/bollywood_movies/similarity_movie.pkl','rb'))

st.title('Bollywood Movie Recommender')
df=pd.DataFrame(df)
movie_name=st.selectbox('Write the Movie Name here',df['title'].values)

if st.button('Recommend'):
    name,poster=pred(movie_name)

    col1,col2,col3=st.columns(3)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])

    col4,col5,col6=st.columns(3)
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])
        
