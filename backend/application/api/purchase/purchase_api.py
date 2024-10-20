from datetime import datetime, timedelta, timezone

from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model
from flask import jsonify
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


game_user_fields = {
    'userid': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'gameid': fields.Integer,
    'game_title': fields.String,
    'date': fields.DateTime,
    'purchased': fields.Boolean,
    'subscribed': fields.Boolean,
    'completed': fields.Boolean
}


user_parser = reqparse.RequestParser()
user_parser.add_argument(
    'userid', type=int, help="User ID is required !")


def current_time():
    current_timeutc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    current_time = current_timeutc + ist_offset
    return current_time


def month_subscribe(dt):
    ist_offset = timedelta(days=30)
    current_time = dt + ist_offset
    return current_time


class CheckPurchase(Resource):
    def get(self, userid, gameid):
        gu = gu_model.query.filter_by(userid=userid, gameid=gameid).first()
        if gu.purchased:
            return {'status': 'success',
                    'message': "You have purchased this game",
                    'type': 'purchase'}
        elif gu.subscribed:
            return {'status': 'success',
                    'message': "You have subscribed to this game",
                    'type': 'subscribe'}
        elif gu.completed:
            return {'status': 'success',
                    'message': "You have completed this game",
                    'type': 'completed'}
        else:
            return {'status': 'failure',
                    'message': "You have no access to this game",
                    'type': 'no access'}


class PurchaseResource(Resource):
    def get(self, userid, gameid):
        gu = gu_model.query.filter_by(userid=userid, gameid=gameid).first()
        if gu and gu.purchased:
            return {'status': 'failure',
                    'message': "You have already purchased this game",
                    'type': 'already purchased'}
        pur = gu_model(userid=userid, gameid=gameid, purchased=True)
        db.session.add(pur)
        db.session.commit()
        return {'status': 'success',
                'message': "You have purchased this game",
                'type': 'purchased'}


class GetPurchasedResource(Resource):
    def get(self):
        uid = user_parser.parse_args().get('userid')
        if not uid:
            return {'status': 'failure',
                    'message': "User not found"}
        if user_model.query.filter_by(id=int(uid)).first().roles[0].name != 'user':
            return {'status': 'failure',
                    'message': "unauthorized"}
        else:
            purchased_games = db.session.query(gu_model, game_model, user_model)\
                .join(game_model, gu_model.gameid == game_model.id)\
                .join(user_model, gu_model.userid == user_model.id)\
                .filter(gu_model.userid == uid, gu_model.purchased == True).all()

            result = [{
                'userid': user.id,
                'username': user.username,
                'email': user.email,
                'gameid': game.id,
                'game_title': game.title,
                'date': game_user.date,
                'purchased': game_user.purchased,
                'subscribed': game_user.subscribed,
                'completed': game_user.completed
            } for game_user, game, user in purchased_games]
        return {'status': 'success', 'purchased': marshal(result, game_user_fields)}


class GetAllPurchasedResource(Resource):
    def get(self):
        uid = user_parser.parse_args().get('userid')
        if not uid:
            return {'status': 'failure',
                    'message': "User not found"}
        if user_model.query.filter_by(id=int(uid)).first().roles[0].name != 'admin' or uid != 1:
            return {'status': 'failure',
                    'message': "unauthorized"}
        else:
            purchased_games = db.session.query(gu_model, game_model, user_model)\
                .join(game_model, gu_model.gameid == game_model.id)\
                .join(user_model, gu_model.userid == user_model.id)\
                .filter(gu_model.userid == uid, gu_model.purchased == True).all()

            result = [{
                'userid': user.id,
                'username': user.username,
                'email': user.email,
                'gameid': game.id,
                'game_title': game.title,
                'date': game_user.date,
                'purchased': game_user.purchased,
                'subscribed': game_user.subscribed,
                'completed': game_user.completed
            } for game_user, game, user in purchased_games]
        return {'status': 'success', 'purchased': marshal(result, game_user_fields)}
