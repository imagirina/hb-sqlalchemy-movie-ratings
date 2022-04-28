"""Server for movie ratings app."""

from flask import Flask, render_template, request, session, redirect, flash
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Homepage Route
@app.route('/')
def homepage():
    return render_template('homepage.html')


# Movies route (list of movies)
@app.route('/movies')
def all_movies():
    movies = crud.get_movies()

    return render_template('movies.html', movies = movies)

# Show details of particular movie
@app.route('/movies/<movie_id>')
def movie_details(movie_id):    
    movie_details = crud.get_movie_details(movie_id)
    
    return render_template('movie_details.html', movie=movie_details)


# Users route (list of users)
@app.route('/users')
def all_users():
    users = crud.get_users()

    return render_template('users.html', users = users)


# Show details of particulat user
@app.route('/users/<user_id>')
def user_details(user_id):
    user_details = crud.get_user_details(user_id)

    return render_template("user_details.html", user=user_details)



if __name__ == "__main__":
    # DebugToolbarExtension(app)

    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
