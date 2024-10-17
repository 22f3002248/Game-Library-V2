from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from flask_restx import Resource, fields, marshal, reqparse

genre_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description':fields.String
  # This will be a list of genre titles
}

genres_parser = reqparse.RequestParser()
genres_parser.add_argument(
    'title', type=str, required=True, help="Title is required!"
)
genres_parser.add_argument(
    'description', type=str, location='json', help="Genres must be provided as a list of genre IDs!"
)


class GenreResource(Resource):
    def get(self):
        genres = genre_model.query.all()
        return {'status': 'success', 'games': marshal(genres, genre_fields)}

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


