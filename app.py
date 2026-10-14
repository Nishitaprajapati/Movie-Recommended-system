import streamlit as st
import pickle
import pandas as pd
import requests
#
# def fetch_poster(movie_id):
#     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data=response.json()
#     print(data)
#     return "https://image/tmdb.org/t/p/w506/"+data['poster_path']
def recommend(movie):
    if movie not in movies['title'].values:
        print(f"Movie '{movie}' not found in the dataset.")
        return

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from Api
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return  recommended_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'How would you like to be contacted',
    movies['title'].values
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.markdown(f"<h2 style='text-align: center; font-size: 15px;'>{names[0]}</h2>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.markdown(f"<h2 style='text-align: center; font-size: 15px;'>{names[1]}</h2>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col3:
        st.markdown(f"<h2 style='text-align: center; font-size: 15px;'>{names[2]}</h2>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col4:
        st.markdown(f"<h2 style='text-align: center; font-size: 15px;'>{names[3]}</h2>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col5:
        st.markdown(f"<h2 style='text-align: center; font-size: 15px;'>{names[4]}</h2>", unsafe_allow_html=True)
        st.image("https://static.streamlit.io/examples/cat.jpg")