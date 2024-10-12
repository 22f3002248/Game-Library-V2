from datetime import datetime, timedelta, timezone

from flask_security import RoleMixin, UserMixin

from .database import db

current_timeutc = datetime.now(timezone.utc)
ist_offset = timedelta(hours=5, minutes=30)
current_time = current_timeutc + ist_offset

# ? id, title, genre, played
game_genre_association = db.Table('game_genre',
                                  db.Column('game_id', db.Integer, db.ForeignKey(
                                      'game.id'), primary_key=True),
                                  db.Column('genre_id', db.Integer, db.ForeignKey(
                                      'genre.id'), primary_key=True)
                                  )


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    # genre = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    developer = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    platform = db.Column(db.String(50))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    multiplayer = db.Column(db.Boolean, default=False)
    no_of_downloads = db.Column(db.Integer, default=0)
    genres = db.relationship(
        'Genre', secondary=game_genre_association, backref='games', lazy=True)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text)


'''
class category():....
'''

# ---------------------------------------TOUR GUIDE----------------------------------


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))

    # functions
