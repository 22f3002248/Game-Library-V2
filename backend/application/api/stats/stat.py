import os
from datetime import datetime

from flask import current_app as app
from flask import request
from flask_restx import Resource, fields, marshal, reqparse

from application.api.game.genre_api import genre_fields
from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as game_user_model
from application.data.model import GamePhoto as game_photos_model
from application.data.model import Genre as genre_model


class UserStats(Resource):
    def get(self, userid):
        purchased_only_games = game_user_model.query.filter_by(user_id=userid,
                                                               purchased=True, subscribed=False).count()

        subscribed_only_games = game_user_model.query.filter_by(user_id=userid,
                                                                subscribed=True, purchased=False).count()
        purchased_completed_games = game_user_model.query.filter_by(user_id=userid,
                                                                    purchased=True, completed=True, subscribed=False).count()
        subscribed_completed_games = game_user_model.query.filter_by(user_id=userid,
                                                                     subscribed=True, completed=True, purchased=False).count()
        purchased_and_subscribed_games = game_user_model.query.filter_by(user_id=userid,
                                                                         subscribed=True, purchased=True).count()
        purchased_and_subscribed_completed_games = game_user_model.query.filter_by(user_id=userid,
                                                                                   purchased=True, completed=True, subscribed=True).count()

        total = game_model.query.count()
        completed_games = game_user_model.query.filter_by(user_id=userid,
                                                          completed=True).count()
        print(purchased_only_games, completed_games, subscribed_only_games,
              purchased_completed_games, subscribed_completed_games, total)
        return {'status': 'success', 'data': {'purchased': purchased_only_games,
                                              'purchased_completed': purchased_completed_games,
                                              'subscribed_completed': subscribed_completed_games,
                                              'completed': completed_games,
                                              'subscribed': subscribed_only_games,
                                              'total': total,
                                              'purchased_and_subscribed': purchased_and_subscribed_games,
                                              'purchased_and_subscribed_completed': purchased_and_subscribed_completed_games}}
