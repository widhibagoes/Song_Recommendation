import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('music_list.csv')
doc_sim_df = pd.read_csv('similarity.csv')

musics_list = df['track_name'].values
artist_name = df['artist_name'].values

def musics_recommender(musics_title, musics=musics_list, artist=artist_name, doc_sims=doc_sim_df):
    # find movie id
    musics_idx = np.where(musics == musics_title)[0][0]
    # get movie similarities
    musics_similarities = doc_sims.iloc[musics_idx].values
    # get top 5 similar movie IDs
    similar_musics_idxs = np.argsort(-musics_similarities)[1:6]
    # get top 5 movies
    similar_musics = musics[similar_musics_idxs]
    similar_artist = artist[similar_musics_idxs]

    similar_data = pd.DataFrame({
        'title': similar_musics,
        'artist': similar_artist
    })
    # return the top 5 movies
    return similar_data

st.title('Sistem Rekomendasi Musik 🎵')
st.header('Menggunakan algoritma TF-IDF dan Cosine Similarity', divider='violet')

user_input = st.text_input('Judul Lagu', '', placeholder='Masukkan judul lagu yang diinginkan')
user_input = user_input.lower()

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    try:
        st.session_state.output = musics_recommender(user_input, musics_list, artist_name, doc_sim_df)
    except:
        st.session_state.output = 'Lagu tidak ditemukan'

st.button('submit', on_click=btn_action)
st.write(st.session_state.output)