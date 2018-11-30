"""Blogly application."""

from flask import Flask, render_template
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = 'SUPER MEGA HYPER SECRET'
DebugToolbarExtension(app)


@app.route('/')
def display_homepage():
    """Displays all users in the Blogly database"""

    users = User.query.all()

    return render_template("homepage.html", users=users)
