"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Consider adding conditionals to run db.create_all()


def connect_db(flask_instance):
    db.app = flask_instance
    db.init_app(flask_instance)


class PostTag(db.Model):
    """ make the m:n table for posts and tags"""

    __tablename__ = 'post_tags'

    post_id = db.Column(
        db.Integer,
        db.ForeignKey('posts.id', ondelete='CASCADE'),
        primary_key=True)
    tag_id = db.Column(
        db.Integer,
        db.ForeignKey('tags.id', ondelete='CASCADE'),
        primary_key=True)


class Post(db.Model):
    """User post"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now())

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False)

    tags = db.relationship('Tag', secondary='post_tags')
    # passive_deletes=True, cascade='all, delete'

    @property
    def post_details(self):
        """Returns the user's full name"""

        name = self.user.full_name
        time = self.created_at.strftime('%a %b %d %Y, %I:%M %p')
        return f"By {name} on {time}."


class User(db.Model):
    """Blogly user"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=True)

    posts = db.relationship(
        'Post', backref='user', passive_deletes=True, cascade='all, delete')

    @property
    def full_name(self):
        """Returns the user's full name"""
        return f"{self.first_name} {self.last_name}"


class Tag(db.Model):
    """ Tags"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship('Post', secondary='post_tags')
