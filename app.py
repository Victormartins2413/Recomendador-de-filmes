import streamlit as st
import pandas as pd

url = "https://raw.githubusercontent.com/Victormartins2413/Recomendador-de-filmes/main/all_movies.csv"
df = pd.read_csv(url)


# Função para exibir as informações do filme
def show_movie_info(title):
    movie = df[df['title_pt'] == title].iloc[0]
    st.write(f"**Título:** {movie['title_pt']}")
    st.write(f"**Gênero:** {movie['genre']}")
    st.write(f"**Ano:** {movie['year']}")
    st.write(f"**Sinopse:** {movie['synopsis']}")

# Configuração do título do webapp
st.title("Sistema de Recomendação de Filmes")

# Campo de seleção de filmes
movie_choice = st.selectbox("Escolha um filme", df['title_pt'])

# Exibir informações quando um filme for escolhido
if st.button("Filtrar"):
    show_movie_info(movie_choice)
