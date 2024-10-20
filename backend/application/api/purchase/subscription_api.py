from datetime import datetime, timedelta, timezone

from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Subscription as sub_model
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
        sub = sub_model.query.filter_by(userid=userid).first()
        if sub:
            return {'status': 'success', 'subscription_status': 'active', 'end_date': str(sub.end_date)}
        else:
            return {'status': 'failure', 'message': "user is not subscribed"}


class SubscriptionResource(Resource):
    def get(self, userid):
        sub = sub_model.query.filter_by(userid=userid).first()
        if sub:
            sub.start_date = current_time()
            sub.end_date = month_subscribe(current_time())
            db.session.commit()
            return {'status': 'success', 'subscription_status': 'active-updated', 'end_date': str(sub.end_date)}
        else:
            sub = sub_model(userid=userid)
            db.session.add()
            db.session.commit()
            return {'status': 'failure', 'message': "user is not subscribed"}
