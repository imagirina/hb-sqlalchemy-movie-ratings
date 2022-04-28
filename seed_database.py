"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import model
import crud
import server

# Telling Python to run the dropdb and create_all commands using os.system
os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
# Create the tables (from model.py)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []

# Create movies, store them in a movies_in_db (we will use them to create fake ratings)
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']

    # Converting release_date to a datetime object
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

    # Creating a movie and appending it to movies_in_db
    new_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(new_movie)

# Adding movies to the SQLAlchemy session
model.db.session.add_all(movies_in_db)

# Create 10 random users; for each user, create 10 ratings on random movies with random scores
users_in_db = []
for n in range(10):
    email = f'user{n}@test.com'  # A unique email!
    password = 'test'

    # Creating a user
    new_user = crud.create_user(email, password)
    model.db.session.add(new_user)

    # Creating 10 ratings for the user
    for _ in range(10):
        score = randint(1,5)
        random_movie = choice(movies_in_db)
        new_rating = crud.create_rating(score, random_movie, new_user)
        model.db.session.add(new_rating)

model.db.session.commit()