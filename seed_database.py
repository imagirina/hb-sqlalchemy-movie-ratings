"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import model
import crud
import server

os.system("dropdb ratings")
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


with open('data/movies.jason') as f:
    movie_data = json.loads(f.read())

