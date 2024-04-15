from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from typing import Union

app = FastAPI()
app.title = "FastAPI"
app.version = "0.1.0"
NAMESPACE_TAG = 'movie'

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2019',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Spiderman',
        'overview': "Spiderman 2 la pelea con octopus",
        'year': '2009',
        'rating': 7.8,
        'category': 'Drama'    
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse(
        '<h1>Hello world</h1>'
    )

@app.get('/movies', tags=[NAMESPACE_TAG])
def get_movies(category: Union[str, None] = None, year: Union[int, None]=None):
    movies_filtered = movies
    if category:
        movies_filtered = [movie for movie in movies if movie.get('category').lower() == category.lower()]
    if year:
        movies_filtered = [movie for movie in movies if movie.get('year') == str(year)]
    
    return movies_filtered

@app.get('/movies{id}', tags=[NAMESPACE_TAG])
def get_movie(id_movie: int):
    return [movie for movie in movies if movie['id'] == id_movie]

@app.post('/movies', tags=[NAMESPACE_TAG])
def create_movie(
        id: int = Body(),
        title: str = Body(),
        overview: str = Body(),
        year: int = Body(),
        rating: int = Body(),
        category: str = Body()
    ):
    movies.append({
        'id': id,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    })
    return movies.sort()

@app.put('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def update_movie(
        id_movie: int,
        title: str = Body(),
        overview: str = Body(),
        year: int = Body(),
        rating: int = Body(),
        category: str = Body()
    ):
    print(movies)
    movie = [m for m in movies if m.get('id') == id_movie]
    movie_index = movies.index(movie[0])
    movie = {
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    }
    movies.__setitem__(movie_index, movie)
    return movies

@app.delete('/movies/{id}', tags=[NAMESPACE_TAG])
def delete_movie(id_movie: int):
    movie = [m for m in movies if m.get('id') == id_movie]
    movies.remove(movie[0])
    return movies
