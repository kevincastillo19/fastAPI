"""
    This module is for handle all Movie's methods
"""
from services.movie import MovieService
from config.database import Session
from schemas.movie import Movie

class TestMovie:
    """Args to test all methods
    """
    movie = Movie(
        **{
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2019',
        'rating': 7.8,
        'category': 'Acción'    
        }
    )
    
    def test_create_movie(self):
        """This method test Movie creation with default args
        
        Keyword arguments:
        args -- Movie schema
        Return: None
        """
        db = Session()
        new_movie = MovieService(db).create_movie(self.movie)
        assert new_movie is not None
        assert hasattr(new_movie, 'title')
        assert new_movie.rating == 7.8
        assert new_movie.year == 2019
        
    def test_get_movies(self) -> None:
        """This method test a get_movies function from Movie's model.
        """
        db = Session()
        response = MovieService(db).get_movies(self.movie.__dict__)
        assert isinstance(response, list)
        assert self.movie.category == response[0].category
    
    # def test_update_movie(self):
    #     """This method test update functionallity for Movie's model
    #     """
    #     db = Session()                
    #     response = MovieService(db).update_movie(self.movie)
    