from datetime import datetime

from application.data.database import db
from application.data.datalist import GAMES, GENRES
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import User as user_model
from application.data.model import game_genre_association as gg_model
from werkzeug.security import generate_password_hash

#changes have to do
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
    if not ds.find_user(email="user.gamevault@gmail.com"):
        ds.create_user(username="user1", email="user.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["user"])
        db.session.commit()
    if not game_model.query.all():
        for i in GAMES:
            release_date = datetime.strptime(
                i["release_date"], "%Y-%m-%d").date()
            new_game = game_model(
                title=i["title"],
                genre=i["genre"],
                release_date=release_date,
                developer=i["developer"],
                publisher=i["publisher"],
                platform=i["platform"],
                rating=i["rating"],
                description=i["description"],
                price=i["price"],
                multiplayer=i["multiplayer"],
                no_of_downloads=i["no_of_downloads"]
            )

            db.session.add(new_game)
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
