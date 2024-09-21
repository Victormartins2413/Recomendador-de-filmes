import streamlit as st
import pandas as pd

# Tente carregar o CSV
try:
    df = pd.read_csv("data/all_movies.csv", delimiter=';')  # Ajuste o delimitador conforme o formato real do CSV
except Exception as e:
    st.error(f"Erro ao ler o arquivo CSV: {e}")

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
if 'title_pt' in df.columns:
    movie_choice = st.selectbox("Escolha um filme", df['title_pt'])

    # Exibir informações quando um filme for escolhido
    if st.button("Filtrar"):
        show_movie_info(movie_choice)
else:
    st.error("Coluna 'title_pt' não encontrada no DataFrame.")
