import streamlit as st
import pandas as pd

# Tente carregar o CSV
try:
    df = pd.read_csv("all_movies.csv", delimiter=';')
    st.write("Colunas disponíveis:", df.columns.tolist())  # Verifique as colunas
except Exception as e:
    st.error(f"Erro ao ler o arquivo CSV: {e}")
    df = pd.DataFrame()  # Inicializa um DataFrame vazio para evitar NameError

# Função para exibir as informações do filme
def show_movie_info(title):
    movie = df[df['title_pt'] == title].iloc[0]
    st.write(f"**Título:** {movie['title_pt']}")
    st.write(f"**Gênero:** {movie['genre']}")
    st.write(f"**Ano:** {movie['year']}")
    if 'sinopse' in movie:  # Verifique se a coluna existe
        st.write(f"**Sinopse:** {movie['sinopse']}")
    else:
        st.write("**Sinopse:** Não disponível.")

# Configuração do título do webapp
st.title("Sistema de Recomendação de Filmes")

if not df.empty and 'title_pt' in df.columns:
    movie_choice = st.selectbox("Escolha um filme", df['title_pt'])

    # Exibir informações quando um filme for escolhido
    if st.button("Filtrar"):
        show_movie_info(movie_choice)

# Renderizar o HTML
st.subheader("Detalhes dos Filmes")
try:
    # Carregar o conteúdo do arquivo HTML
    with open("Filmes.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600)  # Ajuste a altura conforme necessário
except FileNotFoundError:
    st.error("Arquivo HTML 'Filmes.html' não encontrado.")
