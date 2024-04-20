from fastapi import APIRouter, Path, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from app.config.database import Session
from app.models.movie import Movie as MovieModel
from app.middlewares.jwt_bearer import JWTBearer
from app.services.movie import MovieService
from app.schemas.movie import Movie

movie_router = APIRouter()
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

@movie_router.get('/movies', tags=[NAMESPACE_TAG], response_model=List[Movie], dependencies=[Depends(JWTBearer())])
def get_movies(category: Optional[str] = Query(default=None), year: Optional[int]=Query(default=None)) -> List[Movie]:
    db = Session()
    response = MovieService(db).get_movies({'category':category, 'year': year})
    return JSONResponse(content=jsonable_encoder(response))

@movie_router.get('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def get_movie(id_movie: int = Path(ge=1, le=20)):
    db = Session()
    movie = MovieService(db).get_movie(id_movie)
    if movie:
        return JSONResponse(content=jsonable_encoder(movie))
    raise HTTPException(404, "No encontrado")

@movie_router.post('/movies',
    tags=[NAMESPACE_TAG],
    response_model=List[Movie],
    dependencies=[Depends(JWTBearer())]
)
def create_movie(movie: Movie):
    db = Session()
    new_movie = MovieService(db).create_movie(movie)    
    return JSONResponse(status_code=201, content={'id': new_movie.id})

@movie_router.put('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def update_movie(id_movie: int, movie: Movie):
    db = Session()
    movie_updated = MovieService(db).update_movie(id_movie, movie)
    return JSONResponse(status_code=200, content={'success':True, 'id':movie_updated.id})

@movie_router.delete('/movies/{id}', tags=[NAMESPACE_TAG])
def delete_movie(id_movie: int):
    db = Session()
    movie = MovieService(db).delete_movie(id_movie)
    if not movie:
        raise HTTPException(404, "No existe")    
    response = jsonable_encoder(movie)
    return JSONResponse(content=response)
