from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = "FastAPI"
app.version = "0.1.0"
NAMESPACE_TAG = 'movie'

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Película", max_length=15)
    overview: Optional[str] = Field(default="Resumen", max_length=100, min_length=5)
    year: int = Field(le=2024, default=2024)
    rating: Optional[float] = Field(ge=0)
    category: str = Field(max_length='15')
    

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

@app.get('/movies', tags=[NAMESPACE_TAG], response_model=List[Movie])
def get_movies(category: Optional[str] = Query(default=None), year: Optional[int]=Query(default=None)) -> List[Movie]:
    movies_filtered = movies
    print(category, year)
    if category:
        movies_filtered = [movie for movie in movies if movie.get('category').lower() == category.lower()]
    if year:
        movies_filtered = [movie for movie in movies if movie.get('year') == str(year)]
    return JSONResponse(content=movies_filtered)

@app.get('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def get_movie(id_movie: int = Path(ge=1, le=20)):
    return JSONResponse(content=[movie for movie in movies if movie['id'] == id_movie])

@app.post('/movies', tags=[NAMESPACE_TAG], response_model=List[Movie] )
def create_movie(movie: Movie):
    movies.append(movie)
    response = jsonable_encoder(movies)
    return JSONResponse(status_code=201, content=response)

@app.put('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def update_movie(id_movie: int, movie: Movie):
    movie = [m for m in movies if m.get('id') == id_movie]
    movie_index = movies.index(movie[0])
    movies.__setitem__(movie_index, movie)
    return JSONResponse(status_code=200, content=movie)

@app.delete('/movies/{id}', tags=[NAMESPACE_TAG])
def delete_movie(id_movie: int):
    movie = [m for m in movies if m.get('id') == id_movie]
    movies.remove(movie[0])
    JSONResponse(content=movies)
