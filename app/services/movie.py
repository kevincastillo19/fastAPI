"""
Movie Service Module
This module contains the MovieService class which provides methods to interact with the MovieModel.
"""

from app.models.movie import Movie as MovieModel
from typing import List
from app.schemas.movie import Movie


class MovieService:
    """
    Service class to handle operations related to movies.
    """

    def __init__(self, db) -> None:
        """
        Initialize the MovieService with a database session.

        Args:
            db: The database session to be used for queries.
        """
        self.db = db

    def get_movies(self, params: dict) -> List[MovieModel]:
        """
        Retrieve a list of movies based on filter parameters.

        Args:
            params (dict): A dictionary containing filter parameters such as 'category' and 'year'.

        Returns:
            List[MovieModel]: A list of movies matching the filter criteria.
        """
        result = self.db.query(MovieModel)
        if params.get("category"):
            result = result.filter_by(category=params.get("category"))
        if params.get("year"):
            result = result.filter_by(year=params.get("year"))
        return result.all()

    def get_movie(self, id_movie: int) -> MovieModel:
        """
        Retrieve a single movie by its ID.

        Args:
            id_movie (int): The ID of the movie to retrieve.

        Returns:
            MovieModel: The movie object if found, otherwise None.
        """
        result = self.db.query(MovieModel).filter_by(id=id_movie).first()
        return result

    def create_movie(self, movie: Movie) -> Movie:
        """
        Create a new movie in the database.

        Args:
            movie (Movie): The movie data to be created.

        Returns:
            Movie: The newly created movie object.
        """
        new_movie = MovieModel(**movie.__dict__)
        self.db.add(new_movie)
        self.db.commit()
        return new_movie

    def update_movie(self, id_movie: int, data: Movie) -> Movie:
        """
        Update an existing movie in the database.

        Args:
            id_movie (int): The ID of the movie to update.
            data (Movie): The updated movie data.

        Returns:
            Movie: The updated movie object if found, otherwise None.
        """
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
        """
        Delete a movie from the database.

        Args:
            id_movie (int): The ID of the movie to delete.

        Returns:
            MovieModel: The deleted movie object if found, otherwise None.
        """
        _movie = self.db.query(MovieModel).filter(MovieModel.id == id_movie).first()
        if not _movie:
            return None
        self.db.delete(_movie)
        self.db.commit()
        return _movie
