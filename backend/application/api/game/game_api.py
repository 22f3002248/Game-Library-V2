from application.data.database import db
from application.data.model import Game as game_model
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


games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'title', type=str, help="Title is required !")
games_parser.add_argument(
    'genre', type=str, help="Genre is required !")
games_parser.add_argument(
    'played', type=bool, help="played can be given optionally !")


class GameResource(Resource):
    # ? to send all the games
    def get(self):
        games = game_model.query.all()
        return {'status': 'success', 'games': marshal(games, game_fields)}

    def post(self):
        args = games_parser.parse_args()
        title = args.get('title')
        if not title:
            return {"status": 'failure', 'message': 'game title is required !'}, 400
        genre = args.get('genre')

        new_game = game_model(title=title, genre=genre)
        db.session.add(new_game)
        db.session.commit()
        return {"status": 'success', 'message': 'game is added !'}


class SingleGameResource(Resource):
    # ? to send all the games
    def get(self, id):
        games = game_model.query.filter_by(id=id).first()
        return {'status': 'success', 'game': marshal(games, game_fields)}

    def put(self, id):
        # print('here !')
        args = games_parser.parse_args()
        game = game_model.query.filter_by(id=id).first()
        if not game:
            return {"status": 'failure', 'message': 'game not found !'}, 404
        title = game.title
        genre = game.genre
        played = game.played
        if args.get('title'):
            title = args.get('title')
        if args.get('genre'):
            genre = args.get('genre')
        game.title = title
        game.genre = genre
        game.played = played
        db.session.commit()
        return {"status": 'success', 'message': 'game is updated !'}

    def delete(self, id):
        game = game_model.query.filter_by(id=id).first()
        if not game:
            return {"status": "failure", "message": "game not found!"}, 404
        db.session.delete(game)
        db.session.commit()
        return {"status": "success", "message": "game deleted!"}, 200


class TopGameListResource(Resource):
    def get(self, no):
        if no < 1:
            return {"status": "failure", "message": "games not found!"}
        games = game_model.query.order_by(game_model.rating.desc()).all()
        games = games[:no]
        if len(games) < 1:
            return {"status": "failure", "message": "games not found!"}
        return {'status': 'success', 'games': marshal(games, game_fields)}
