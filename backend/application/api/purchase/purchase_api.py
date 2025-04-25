from datetime import datetime, timedelta, timezone

from flask import jsonify
from flask_restx import Resource, fields, marshal, reqparse

from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model

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
        gu = gu_model.query.filter_by(user_id=userid, game_id=gameid).first()
        return {"status": "success", "purchased": gu.purchased,
                "subscribed": gu.subscribed, "completed": gu.completed}


class PurchaseResource(Resource):
    def get(self, userid, gameid):
        gu = gu_model.query.filter_by(userid=userid, gameid=gameid).first()
        if gu.purchased:
            return {'status': 'failure',
                    'message': "You have already purchased this game",
                    'type': 'already purchased'}
        if gu:
            gu.purchased = True
            db.session.commit()
        else:
            pur = gu_model(userid=userid, gameid=gameid, purchased=True)
            db.session.add(pur)
            db.session.commit()
        return {'status': 'success',
                'message': "You have purchased this game",
                'type': 'purchased'}


class GetPurchasedResource(Resource):
    def get(self, uid):
        if not uid:
            return {'status': 'failure',
                    'message': "User not found"}
        purchased_games = gu_model.query.filter_by(
            user_id=uid, purchased=True).all()
        games = []
        for i in purchased_games:
            game = game_model.query.filter_by(id=i.game_id).first()
            games.append(game)
        print(games)
        return {'status': 'success', 'games': marshal(games, game_fields)}


class GetAllPurchasedResource(Resource):
    def get(self, userid):
        user = user_model.query.filter_by(id=userid).first()
        if not user:
            return {'status': 'failure', 'message': "User not found"}, 404
        if user.roles[0].name != 'admin':
            return {'status': 'failure', 'message': "Unauthorized"}, 403
        purchased_games = db.session.query(gu_model, game_model, user_model)\
            .join(game_model, gu_model.gameid == game_model.id)\
            .join(user_model, gu_model.userid == user_model.id)\
            .filter(gu_model.purchased == True).all()
        result = [{
            'userid': user.id,
            'username': user.username,
            'email': user.email,
            'gameid': game.id,
            'game_title': game.title,
            'date': game_user.date.strftime('%Y-%m-%d %H:%M:%S'),
            'purchased': game_user.purchased,
            'subscribed': game_user.subscribed,
            'completed': game_user.completed
        } for game_user, game, user in purchased_games]

        return {'status': 'success', 'purchased': marshal(result, game_user_fields)}
