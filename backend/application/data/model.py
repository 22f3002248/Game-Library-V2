import os
from datetime import datetime, timedelta, timezone

from flask import current_app as app
from flask import url_for
from flask_security import RoleMixin, UserMixin

from .database import db


def current_time():
    current_timeutc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    current_time = current_timeutc + ist_offset
    return current_time


def month_subscribe(dt):
    ist_offset = timedelta(days=30)
    current_time = dt + ist_offset
    return current_time


game_genre_association = db.Table('game_genre',
                                  db.Column('game_id', db.Integer, db.ForeignKey(
                                      'game.id'), primary_key=True),
                                  db.Column('genre_id', db.Integer, db.ForeignKey(
                                      'genre.id'), primary_key=True)
                                  )


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)
    developer = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    platform = db.Column(db.String(50))
    rating = db.Column(db.Float)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    multiplayer = db.Column(db.Boolean, default=False)
    no_of_downloads = db.Column(db.Integer, default=0)
    played = db.Column(db.Boolean, default=False)
    genres = db.relationship(
        'Genre', secondary=game_genre_association, backref='games', lazy=True)
    users = db.relationship('Game_User', back_populates='game')
    reviews = db.relationship('Review', back_populates='game')

    def get_cover_image(self):
        cover_filename = f"{self.id}.jpg"
        cover_path = os.path.join(
            app.root_path, app.config['STATIC_FOLDER'], 'game_posters', cover_filename)
        if not os.path.exists(cover_path):
            cover_filename = "NoCover.jpg"
        cover_url = url_for(
            'static', filename=f'game_posters/{cover_filename}', _external=True)
        return cover_url


class GamePhoto(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    game_title = db.Column(db.Text, default=None)
    picture1 = db.Column(db.Text, default=None)
    picture2 = db.Column(db.Text, default=None)
    picture3 = db.Column(db.Text, default=None)
    picture4 = db.Column(db.Text, default=None)
    picture5 = db.Column(db.Text, default=None)
    game = db.relationship('Game', backref='photos')


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=True)


class Subscription(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    start_date = db.Column(db.DateTime, default=current_time())
    end_date = db.Column(db.DateTime, default=month_subscribe(current_time()))


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
    games = db.relationship('Game_User', back_populates='user')
    reviews = db.relationship('Review', back_populates='user')


class Game_User(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    purchased = db.Column(db.Boolean, default=False)
    subscribed = db.Column(db.Boolean, default=False)
    completed = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime, default=current_time())

    # Relationships back to Game and User
    game = db.relationship('Game', back_populates='users')
    user = db.relationship('User', back_populates='games')


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    date = db.Column(db.DateTime, default=current_time())
    game = db.relationship('Game', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')
