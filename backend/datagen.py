from datetime import datetime
from application.data.database import db
from application.data.datalist import GAMES
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import User as user_model
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
    if not ds.find_user(email="user.gamevault@gmail.com"):
        ds.create_user(username="user1", email="user.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["user"])
        db.session.commit()
    games = game_model.query.all()
    if not games:
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
