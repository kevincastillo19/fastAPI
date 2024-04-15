from models.movie import Movie as MovieModel
from typing import List
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

        
            