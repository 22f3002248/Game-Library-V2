from datetime import datetime

from application.data.database import db
from application.data.datalist import GAMES, GENRES
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Genre as genre_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model
from application.data.model import game_genre_association as gg_model
from werkzeug.security import generate_password_hash


def gen():
    ds.find_or_create_role(
        name="admin", description="Admin manages the system")
    ds.find_or_create_role(
        name="user", description="User interacts with the system")
    db.session.commit()
    if not ds.find_user(email="manager.gamevault@gmail.com"):
        ds.create_user(username="manager", email="manager.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["admin"])
        db.session.commit()

    if not ds.find_user(email=f"user.gamevault@gmail.com"):
        ds.create_user(username=f"user", email=f"user.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["user"])
        db.session.commit()
    for i in range(2, 11):
        if not ds.find_user(email=f"user{i}.gamevault@gmail.com"):
            ds.create_user(username=f"user{i}", email=f"user{i}.gamevault@gmail.com",
                           password=generate_password_hash("12345"), roles=["user"])
            db.session.commit()
            if i % 2 == 0:
                sub = sub_model(userid=user_model.query.filter_by(
                    username=f"user{i}").first().id)
                db.session.add(sub)
                db.session.commit()
        db.session.commit()


def create_genres():
    if not genre_model.query.all():
        for genre_data in GENRES:
            genre = genre_model.query.filter_by(
                title=genre_data["title"]).first()
            if not genre:
                new_genre = genre_model(
                    title=genre_data["title"], desc=genre_data["desc"])
                db.session.add(new_genre)
        db.session.commit()


def create_games():
    if not game_model.query.all():
        for game_data in GAMES:
            release_date = datetime.strptime(
                game_data["release_date"], "%Y-%m-%d").date()
            new_game = game_model(
                title=game_data["title"],
                release_date=release_date,
                developer=game_data["developer"],
                publisher=game_data["publisher"],
                platform=game_data["platform"],
                rating=game_data["rating"],
                description=game_data["description"],
                price=game_data["price"],
                multiplayer=game_data["multiplayer"],
                no_of_downloads=game_data["no_of_downloads"]
            )
            db.session.add(new_game)
            for genre_title in game_data["genres"]:
                genre = genre_model.query.filter_by(title=genre_title).first()
                if genre:
                    new_game.genres.append(genre)

        db.session.commit()
