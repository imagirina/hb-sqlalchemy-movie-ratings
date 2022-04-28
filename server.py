"""Server for movie ratings app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    
    # from model import connect_to_db#
    # connect_to_db(app, "ratings")#

    app.run(host="0.0.0.0", debug=True)
