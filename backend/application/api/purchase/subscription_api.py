import hashlib
from datetime import datetime, timedelta, timezone

from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Subscription
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model
from flask_restx import Resource, fields, marshal, reqparse

genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String
}

game_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'genres': fields.List(fields.Nested(genre_fields)),
    'release_date': fields.String,
    'developer': fields.String,
    'publisher': fields.String,
    'platform': fields.String,
    'rating': fields.Float,
    'description': fields.String,
    'price': fields.Float,
    'multiplayer': fields.Boolean,
    'no_of_downloads': fields.Integer,
    'played': fields.Boolean,
    'poster': fields.String(attribute=lambda x: x.get_cover_image())
}

sub_fields = {
    'username': fields.String,
    'email': fields.String,
    'subscription_date': fields.DateTime,
    'subscription_end_date': fields.DateTime,
    'subscription_status': fields.Boolean,
}


def current_time():
    current_timeutc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    current_time = current_timeutc + ist_offset
    return current_time


def month_subscribe(dt):
    ist_offset = timedelta(days=30)
    current_time = dt + ist_offset
    return current_time


games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'title', type=str, help="Title is required !")
games_parser.add_argument(
    'genre', type=str, help="Genre is required !")
games_parser.add_argument(
    'played', type=bool, help="played can be given optionally !")


class CheckSubscription(Resource):
    def get(self, userid):
        sub = sub_model.query.filter_by(
            userid=userid, subscription_status=True).first()
        if sub:
            return {'status': 'success', 'subscription': True, 'end_date': str(sub.subscription_end_date)}
        else:
            return {'status': 'failure', 'subscription': False}


class SubscriptionResource(Resource):
    def get(self, userid):  # add one more month
        sub = sub_model.query.filter_by(userid=userid).first()
        if sub:
            if sub.subscription_status == False:
                sub.subscription_date = current_time()
                sub.subscription_end_date = month_subscribe(current_time())
            else:
                sub.subscription_end_date = sub.subscription_end_date + \
                    timedelta(days=30)
            db.session.commit()
            return {'status': 'success', 'subscription': True, 'end_date': str(sub.subscription_end_date)}
        else:
            sub = sub_model(userid=userid, subscription_date=current_time(),
                            subscription_end_date=month_subscribe(
                                current_time()),
                            subscription_status=True)
            db.session.add()
            db.session.commit()
            return {'status': 'failure', 'subscription': True}


class GetSubscribedGames(Resource):
    def get(self, userid):
        sub = sub_model.query.filter_by(
            userid=userid, subscription_status=True).first()
        if not sub:
            return {'status': 'failure', 'message': "No subscription found", 'games': []}
        subscribed_games = gu_model.query.filter_by(
            user_id=userid, subscribed=True).all()
        games = []
        for i in subscribed_games:
            game = game_model.query.filter_by(id=i.game_id).first()
            if game:
                games.append(game)
        if not subscribed_games:
            return {'status': 'failure', 'message': "No games found", 'games': []}
        else:
            return {'status': 'success', 'games': marshal(games, game_fields)}


class GetHash(Resource):
    def get(self, userid, gameid):
        hash = hashlib.sha256(
            str("GAME_HASH"+str(userid)+str(gameid)).encode('utf-8')).hexdigest()
        return {'status': 'success', 'hash': hash}


class GetSubscribedOnlyGames(Resource):
    def get(self, userid):
        sub = sub_model.query.filter_by(
            userid=userid, subscription_status=True).first()
        if not sub:
            return {'status': 'failure', 'message': "No subscription found", 'games': []}
        subscribed_games = gu_model.query.filter_by(
            user_id=userid, subscribed=True, purchased=False).all()
        games = []
        for i in subscribed_games:
            game = game_model.query.filter_by(id=i.game_id).first()
            if game:
                games.append(game)
        if not subscribed_games:
            return {'status': 'failure', 'message': "No games found", 'games': []}
        else:
            return {'status': 'success', 'games': marshal(games, game_fields)}


class GetCompletedGames(Resource):
    def get(self, userid):
        completed_games = gu_model.query.filter_by(
            user_id=userid, completed=True).all()
        li = []
        for i in completed_games:
            li.append(i.game_id)
        if not completed_games:
            return {'status': 'failure', 'message': "No games found", 'games': []}
        else:
            return {'status': 'success', 'games': li}


class SubscribeDownloadGames(Resource):
    def get(self, userid, gameid):
        sub = sub_model.query.filter_by(
            userid=userid, subscription_status=True).first()
        if not sub:
            return {'status': 'failure', 'message': "No subscription found", 'games': []}
        game = gu_model.query.filter_by(
            user_id=userid, game_id=gameid).first()
        if not game:
            game = gu_model(user_id=userid, game_id=gameid, subscribed=True)
            db.session.add(game)
            db.session.commit()
        game.subscribed = True
        db.session.commit()
        return {'status': 'success', 'message': "Game subscribed"}


class AGetSubscribedGames(Resource):
    def get(self):
        subscriptions = sub_model.query.all()
        sub_data = []
        for sub in subscriptions:
            user = user_model.query.filter_by(
                id=sub.userid).first()
            sub_data.append({
                'username': user.username,
                'email': user.email,
                'subscription_date': sub.subscription_date,
                'subscription_end_date': sub.subscription_end_date,
                'subscription_status': sub.subscription_status,
            })
        return {'status': 'success', 'subscriptions': marshal(sub_data, sub_fields)}
