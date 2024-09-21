import streamlit as st

# Renderizar o HTML
st.title("Detalhes dos Filmes")
try:
    # Carregar o conteúdo do arquivo HTML
    with open("Filmes.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600)  # Ajuste a altura conforme necessário
except FileNotFoundError:
    st.error("Arquivo HTML 'Filmes.html' não encontrado.")

