from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from application.data.model import game_genre_association
from flask_restx import Resource, fields, marshal, reqparse
from sqlalchemy import func

genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    # This will be a list of genre titles
}

game_Genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    # This will be a list of genre titles
    'genres': fields.List(fields.String(attribute='title')),
}

genres_parser = reqparse.RequestParser()
genres_parser.add_argument(
    'title', type=str, required=True, help="Title is required!"
)
genres_parser.add_argument(
    'description', type=str, required=True, help="description is required"
)


class AGenreResource(Resource):
    def get(self):
        genres = genre_model.query.all()
        return {'status': 'success', 'genres': marshal(genres, genre_fields)}

    def post(self):
        args = genres_parser.parse_args()
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


class AGenreResource(Resource):
    def get(self):
        genres = genre_model.query.all()
        return {'status': 'success', 'genres': marshal(genres, genre_fields)}

    def post(self):
        args = genres_parser.parse_args()
        title = args.get('title')
        if title:
            new_genre = genre_model(
                title=title,
                description=args['description']
            )
        db.session.add(new_genre)
        db.session.commit()
        return {"status": 'success', 'message': 'genre is added !'}


class AMultipleGenreResource(Resource):
    def get(self, ids):
        # Split the comma-separated string of IDs
        genre_ids = ids.split(',')

        # Convert to integers
        genre_ids = [int(id) for id in genre_ids]

        # Query to get games that match the genre_ids
        filtered_games = (
            game_model.query
            .join(game_genre_association)
            .filter(game_genre_association.c.genre_id.in_(genre_ids))
            .group_by(game_model.id)  # Group by the game ID
            # Only select games with all genres
            .having(func.count(game_genre_association.c.genre_id) == len(genre_ids))
            .all()
        )

        # Use marshal to format the response data
        response_data = [marshal(game, game_Genre_fields)
                         for game in filtered_games]
        if response_data:
            return {'games': response_data}, 200

        else:
            return {'message': 'Game not found'}, 204


class ASingleGenreResource(Resource):
    def delete(self, id):
        genre = genre_model.query.filter_by(id=id).first()
        if not genre:
            # Return a plain dictionary, no need to use jsonify
            return {"status": "failure", "message": "game not found!"}, 404

        # Proceed with deletion if the game is found
        db.session.delete(genre)
        db.session.commit()

        # Return a success response as a plain dictionary
        return {"status": "success", "message": "genre deleted!"}, 200
