"""CRUD operations/utility functions for creating data."""
from model import db, User, Movie, Rating, connect_to_db


# USERS
def create_user(email, password):
    """Create and return a User object."""

    user = User(email=email, password=password)

    return user

def get_users():
    """Return a list of users."""
    
    return User.query.all()

def get_user_details(user_id):
    """Return particular user's details."""
    
    return User.query.get(user_id)


# MOVIES
def create_movie(title, overview, release_date, poster_path):
    """Create and return a Movie object."""

    movie = Movie(title = title, overview = overview, release_date = release_date, poster_path= poster_path)

    return movie


def get_movies():
    """Return a list of movies."""

    return Movie.query.all()

def get_movie_details(movie_id):
    """Return particular movie's details."""

    return Movie.query.get(movie_id)

# RATINGS
def create_rating(score, movie, user):
    """Create and return a Rating object."""

    rating = Rating(score=score, movie=movie, user=user) 

    return rating


if __name__ == '__main__':
    from server import app  
    connect_to_db(app)
