from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Carregar os dados
path_to_export = 'all_movies.csv'  # Ajuste aqui
df = pd.read_csv(path_to_export, sep=';')

@app.route('/')
def index():
    genres = df['genre'].unique()
    return render_template('Filmes.html', genres=genres)

@app.route('/filter', methods=['POST'])
def filter_movies():
    selected_genre = request.form.get('genre')
    selected_title = request.form.get('title')

    filtered_movies = df[(df['genre'] == selected_genre) & (df['title_pt'] == selected_title)]
    return render_template('results.html', movies=filtered_movies)

if __name__ == '__main__':
    app.run()
