from app.models.movie import Movie as MovieModel
from typing import List
from app.schemas.movie import Movie
class MovieService():
    
    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self, params: dict) -> List[MovieModel]:
        result = self.db.query(MovieModel)
        if params.get('category'):
            result = result.filter_by(category=params.get('category'))
        if params.get('year'):
            result = result.filter_by(year=params.get('year'))
        return result.all()
    
    def get_movie(self, id_movie: int) -> MovieModel:
        result = self.db.query(MovieModel).filter_by(id=id_movie).first()        
        return result
    
    def create_movie(self, movie: Movie) -> Movie:
        new_movie = MovieModel(**movie.__dict__)
        self.db.add(new_movie)
        self.db.commit()
        return new_movie
    
    def update_movie(self, id_movie: int, data: Movie) -> Movie:
        _movie = self.db.query(MovieModel).filter(MovieModel.id == id_movie).first()
        if not _movie:
            return None
        for attr, value in data.__dict__.items():
            if value and attr in _movie.__dict__:
                _movie.__setattr__(attr, value)
        self.db.add(_movie)
        self.db.commit()
        return _movie
    
    def delete_movie(self, id_movie: int):
        _movie = self.db.query(MovieModel).filter(MovieModel.id == id_movie).first()
        if not _movie:
            return None
        self.db.delete(_movie)
        self.db.commit()
        return _movie

        
            