from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from application.data.model import game_genre_association
from flask_restx import Resource, fields, marshal, reqparse

genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String
}

genre_fields2 = {
    'id': fields.Integer,
    'title': fields.String,
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

game_Genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    # This will be a list of genre titles
    'genres': fields.List(fields.String(attribute='title')),
    'played': fields.Boolean
}


games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'title', type=str, help="Title is required !")
games_parser.add_argument(
    'genre', type=str, help="Genre is required !")
games_parser.add_argument(
    'played', type=bool, help="played can be given optionally !")

genre_parser = reqparse.RequestParser()
genre_parser.add_argument(
    'title', type=str, help="Title is required !")
genre_parser.add_argument(
    'description', type=str, help="Description is required !")


class GenreResource(Resource):
    def get(self):
        genre = genre_model.query.all()
        return {'status': 'success', 'genres': marshal(genre, genre_fields2)}

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


class GenreResource(Resource):
    def get(self):
        genres = genre_model.query.all()
        return {'status': 'success', 'genres': marshal(genres, genre_fields)}

    def post(self):
        args = genre_parser.parse_args()
        title = args.get('title')
        if title:
            new_genre = genre_model(
                title=title,
                description=args['description']
            )
        db.session.add(new_genre)
        db.session.commit()
        return {"status": 'success', 'message': 'genre is added !'}


class MultipleGenreResource(Resource):
    def get(self, ids):
        # Split the comma-separated string of IDs
        genre_ids = ids.split(',')

        # Convert to integers
        genre_ids = [int(id) for id in genre_ids]

        # Query to get games that match the genre_ids
        filtered_games = game_model.query.join(game_genre_association).filter(
            game_genre_association.c.genre_id.in_(genre_ids)).all()

        # Use marshal to format the response data
        response_data = [marshal(game, game_Genre_fields)
                         for game in filtered_games]

        print(filtered_games)

        return {'games': response_data}, 200
