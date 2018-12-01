"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(flask_instance):
    db.app = flask_instance
    db.init_app(flask_instance)
    # Consider adding conditionals to run db.create_all()


class User(db.Model):
    """Blogly user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=True)

    @property
    def full_name(self):
        """Returns the user's full name"""
        return f"{self.first_name} {self.last_name}"
