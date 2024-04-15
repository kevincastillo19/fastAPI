from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()
app.title = "FastAPI"
app.version = "0.1.0"
NAMESPACE_TAG = 'movie'

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Película", max_length=15)
    overview: Optional[str] = Field(default="Resumen", max_length=100, min_length=10)
    year: int = Field(le=2024, default=2024)
    rating: Optional[float]
    category: str
    

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
def get_movies(category: Optional[str] = None, year: Optional[int]=None):
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
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def update_movie(id_movie: int, movie: Movie):
    movie = [m for m in movies if m.get('id') == id_movie]
    movie_index = movies.index(movie[0])
    movies.__setitem__(movie_index, movie)
    return movies

@app.delete('/movies/{id}', tags=[NAMESPACE_TAG])
def delete_movie(id_movie: int):
    movie = [m for m in movies if m.get('id') == id_movie]
    movies.remove(movie[0])
    return movies
