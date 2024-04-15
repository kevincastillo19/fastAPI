from fastapi import APIRouter, Path, Query, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from config.database import Session
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService

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

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Película", max_length=15)
    overview: Optional[str] = Field(default="Resumen", max_length=100, min_length=5)
    year: int = Field(le=2024, default=2024)
    rating: Optional[float] = Field(ge=0)
    category: str = Field(max_length='15')

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
    new_movie = MovieModel(**movie.__dict__)
    db.add(new_movie)
    db.commit()
    movies = db.query(MovieModel).all()
    response = jsonable_encoder(movies)
    return JSONResponse(status_code=201, content=response)

@movie_router.put('/movies/{id_movie}', tags=[NAMESPACE_TAG])
def update_movie(id_movie: int, movie: Movie):
    db = Session()
    _movie = db.query(MovieModel).filter(MovieModel.id == id_movie).first()
    if not _movie:
        raise HTTPException(404, "No existe")
    for attr, value in movie.__dict__.items():
        if value and attr in _movie.__dict__:
            _movie.__setattr__(attr, value)
    db.add(_movie)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={'success':True})

@movie_router.delete('/movies/{id}', tags=[NAMESPACE_TAG])
def delete_movie(id_movie: int):
    db = Session()
    movie = db.query(MovieModel).filter_by(id=id_movie).first()
    if not movie:
        raise HTTPException(404, "No existe")
    db.delete(movie)
    db.commit()
    movies = jsonable_encoder(db.query(MovieModel).all())
    return JSONResponse(content=movies)
