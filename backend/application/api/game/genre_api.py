from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from application.data.model import game_genre_association
from flask_restx import Resource, fields, marshal, reqparse


genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description':fields.String,
  # This will be a list of genre titles
}

game_Genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'genres': fields.List(fields.String(attribute='title')),  # This will be a list of genre titles
    'played': fields.Boolean
}

genres_parser = reqparse.RequestParser()
genres_parser.add_argument(
    'title', type=str, required=True, help="Title is required!"
)
genres_parser.add_argument(
    'description', type=str, required=True, help="desc is required"
)


class GenreResource(Resource):
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
    def get(self,ids):
         # Split the comma-separated string of IDs
        genre_ids = ids.split(',')
        
        # Convert to integers
        genre_ids = [int(id) for id in genre_ids]
        
        # Query to get games that match the genre_ids
        filtered_games = game_model.query.join(game_genre_association).filter(game_genre_association.c.genre_id.in_(genre_ids)).all()
        
        # Use marshal to format the response data
        response_data = [marshal(game, game_Genre_fields) for game in filtered_games]
        
        print(filtered_games)

        return {'games': response_data}, 200
            
            



