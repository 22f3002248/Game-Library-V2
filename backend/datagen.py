import random
from datetime import datetime, timedelta, timezone

from faker import Faker
from werkzeug.security import generate_password_hash

from application.data.database import db
from application.data.datalist import GAMES, GENRES, feedbacks, game_images
from application.data.datastore import ds
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import GamePhoto as game_photos_model
from application.data.model import Genre as genre_model
from application.data.model import Profile as profile_model
from application.data.model import Review as review_model
from application.data.model import Role as role_model
from application.data.model import RolesUsers as roles_users
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model
from application.data.model import game_genre_association as gg_model


def current_time():
    current_timeutc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    current_time = current_timeutc + ist_offset
    return current_time


def month_subscribe(dt):
    ist_offset = timedelta(days=30)
    current_time = dt + ist_offset
    return current_time


def gen():
    ds.find_or_create_role(
        name="admin", description="Admin manages the system")
    ds.find_or_create_role(
        name="user", description="User interacts with the system")
    db.session.commit()
    if not ds.find_user(email="manager.gamevault@gmail.com"):
        ds.create_user(username="manager", email="manager.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["admin", "user"])
        db.session.commit()

    if not ds.find_user(email=f"user.gamevault@gmail.com"):
        ds.create_user(username=f"user", email=f"user.gamevault@gmail.com",
                       password=generate_password_hash("12345"), roles=["user"])
        db.session.commit()
        sub_model(userid=2)
        sub = sub_model(userid=user_model.query.filter_by(
            username=f"user").first().id, subscription_date=current_time(),
            subscription_end_date=month_subscribe(current_time()),
            subscription_status=True)
        db.session.add(sub)
        db.session.commit()
    for i in range(2, 11):
        if not ds.find_user(email=f"user{i}.gamevault@gmail.com"):
            ds.create_user(username=f"user{i}", email=f"user{i}.gamevault@gmail.com",
                           password=generate_password_hash("12345"), roles=["user"])
            db.session.commit()

            if i % 2 == 0 and i != 2:
                sub = sub_model(userid=user_model.query.filter_by(
                    username=f"user{i}").first().id, subscription_date=current_time(),
                    subscription_end_date=month_subscribe(current_time()),
                    subscription_status=True)
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
                    title=genre_data["title"], description=genre_data["description"])
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


def assign_games_to_users():
    users = user_model.query.all()
    games = game_model.query.all()

    for user in users:
        subscription = sub_model.query.filter_by(userid=user.id).first()
        assigned_games = set()

        # Randomly select some games to assign (e.g., 5 to 10 games)
        num_games_to_assign = random.randint(5, min(len(games), 10))
        selected_games = random.sample(games, num_games_to_assign)

        for game in selected_games:
            if (user.id, game.id) in assigned_games:
                continue

            existing_entry = gu_model.query.filter_by(
                user_id=user.id, game_id=game.id
            ).first()
            if existing_entry:
                continue

            if subscription:
                # Subscribed users may or may not purchase, but they are subscribed
                purchased = random.choice([True, False])
                completed = random.choice([True, False])
                game_user = gu_model(
                    user_id=user.id,
                    game_id=game.id,
                    purchased=purchased,
                    subscribed=True,
                    completed=completed
                )
            else:
                # Non-subscribers may only purchase games
                purchased = random.choice([True, False])
                if not purchased:
                    continue  # skip assigning this game
                completed = random.choice([True, False])
                game_user = gu_model(
                    user_id=user.id,
                    game_id=game.id,
                    purchased=True,
                    subscribed=False,
                    completed=completed
                )

            db.session.add(game_user)
            assigned_games.add((user.id, game.id))

    db.session.commit()


def gen_reviews():
    revs = review_model.query.all()

    if not revs:
        gu = gu_model.query.filter(
            (gu_model.purchased == True) | (gu_model.subscribed == True)
        ).all()

        for i in gu:
            rev = review_model(user_id=i.user_id, game_id=i.game_id,
                               rating=random.randint(2, 5),
                               feedback=random.choice(feedbacks))
            db.session.add(rev)
        db.session.commit()


def create_game_photos():
    if not game_photos_model.query.all():  # Only add if the table is empty
        for game_data in GAMES:
            game = game_model.query.filter_by(title=game_data["title"]).first()
            if game:
                photos_data = game_images.get(game.title)
                if photos_data:
                    # Add up to 5 pictures (if available)
                    new_game_photos = game_photos_model(
                        game_id=game.id,
                        game_title=game.title,
                        picture1=photos_data[0] if len(
                            photos_data) > 0 else None,
                        picture2=photos_data[1] if len(
                            photos_data) > 1 else None,
                        picture3=photos_data[2] if len(
                            photos_data) > 2 else None,
                        picture4=photos_data[3] if len(
                            photos_data) > 3 else None,
                        picture5=photos_data[4] if len(
                            photos_data) > 4 else None
                    )
                    db.session.add(new_game_photos)
        db.session.commit()


fake = Faker('en_IN')  # Use Indian locale for realistic data


def profileDataGen():
    if not profile_model.query.all():
        users = user_model.query.all()

        for user in users:
            # Skip if profile already exists
            if profile_model.query.filter_by(user_id=user.id).first():
                continue

            first_name = fake.first_name()
            last_name = fake.last_name()
            gender = random.choice(['Male', 'Female'])
            dob = fake.date_of_birth(minimum_age=18, maximum_age=40)
            bio = fake.text(max_nb_chars=150)
            profile_picture = f"https://api.dicebear.com/7.x/initials/svg?seed={first_name}{last_name}"

            phone_number = fake.phone_number()
            address = fake.address().replace("\n", ", ")
            city = fake.city()
            state = fake.state()
            country = "India"
            postal_code = fake.postcode()

            github_url = f"https://github.com/{user.username}"
            twitter_url = f"https://twitter.com/{user.username}"
            linkedin_url = f"https://linkedin.com/in/{user.username}"
            website_url = f"https://{user.username}.portfolio.in"

            profile = profile_model(
                user_id=user.id,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                date_of_birth=dob,
                bio=bio,
                profile_picture=profile_picture,
                phone_number=phone_number,
                address=address,
                city=city,
                state=state,
                country=country,
                postal_code=postal_code,
                github_url=github_url,
                twitter_url=twitter_url,
                linkedin_url=linkedin_url,
                website_url=website_url
            )

            db.session.add(profile)

        db.session.commit()
