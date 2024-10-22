from application.api.game.genre_api import genre_fields
from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Genre as genre_model
from flask import request
from flask_restx import Resource, fields, marshal, reqparse

from datetime import datetime
import os
from flask import current_app as app
import base64

game_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'genres': fields.List(fields.String(attribute='title')),
    'release_date': fields.String,
    'developer': fields.String,
    'publisher': fields.String,
    'platform': fields.String,
    'rating': fields.Float,
    'description': fields.String,
    'price': fields.Float,
    'multiplayer': fields.Boolean,
    'no_of_downloads': fields.Integer,
    'poster': fields.String(attribute=lambda x: x.get_cover_image())
    
}



games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'title', type=str, required=True, help="Title is required!"
)
games_parser.add_argument(
    'genre_ids', type=int, action='append', help="Genres must be provided as a list of genre IDs!"
)
games_parser.add_argument(
    'release_date', type=str, required=True, help="release_date is required!"
)
games_parser.add_argument(
    'developer', type=str, required=True, help="developer is required!"
)
games_parser.add_argument(
    'publisher', type=str, required=True, help="publisher is required!"
)
games_parser.add_argument(
    'platform', type=str, required=True, help="platform is required!"
)
games_parser.add_argument(
    'rating', type=float, required=True, help="rating is required!"
)
games_parser.add_argument(
    'description', type=str, required=True, help="description is required!"
)
games_parser.add_argument(
    'price', type=float, required=True, help="price is required!"
)
games_parser.add_argument(
    'multiplayer', type=bool, required=True, help="multiplayer value is required!"
)
games_parser.add_argument(
    'no_of_downloads', type=int, required=True, help="no_of_downloads is required"
)

class GameResource(Resource):
    # ? to send all the games
    def get(self):
        games = game_model.query.all()
        genres = genre_model.query.all()
        return {'status': 'success', 'games': marshal(games, game_fields), 'genres': marshal(genres, genre_fields)}

    def post(self):
        args = games_parser.parse_args()
        title=args['title']
        if title:
            new_game = game_model(
                title=title,
                release_date=args['release_date'],
                developer=args['developer'],
                publisher=args['publisher'],
                platform=args['platform'],
                rating=args['rating'],
                description=args['description'],
                price=args['price'],
                multiplayer=args['multiplayer'],
                no_of_downloads=args['no_of_downloads'], 
            )
        release_date=args['release_date']    
        if isinstance(release_date, str):
            new_game.release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
        genre_ids = args.get('genre_ids', [])
        print("Parsed genre_ids:", genre_ids)  # Debugging line
        if genre_ids:
            # Fetch all genres by their IDs
            genres = genre_model.query.filter(
                genre_model.id.in_(genre_ids)).all()
            new_game.genres = genres
                
        db.session.add(new_game)
        db.session.commit()
        
        #for file 
        print("vgj")
        game = game_model.query.filter_by(title=title).first()   

            # Ensure that game exists before accessing its id
        if not game:
            return {'message': 'Game not found after creation'}, 401

            # Now we know the game exists, so we can safely access game.id
        print(game.id,request.files)
        poster_data = args.get('poster')
        if not poster_data:
            return {'message': 'No poster data provided'}, 400

        # Decode the Base64 string
        header, base64_string = poster_data.split(',', 1)
        file_extension = header.split(';')[0].split('/')[1]  # Extract file extension from header
        new_filename = f"{game.id}.{file_extension}"

        # Save the file to the specified directory
        file_path = os.path.join(app.root_path, app.config['STATIC_FOLDER'], 'game_posters', new_filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Ensure the directory exists

        # Decode and save the image
        with open(file_path, "wb") as fh:
            fh.write(base64.b64decode(base64_string))
        return {'status': 'success', 'message': 'Game is added!'}

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

        if args.get('title'):
            game.title = args['title']

        if args.get('genre_ids'):
            genre_ids = args['genre_ids']
            genres = genre_model.query.filter(
                genre_model.id.in_(genre_ids)).all()
            game.genres = genres  # Associate new genres

        if args.get('played') is not None:  # Check if played is provided
            game.played = args['played']

        db.session.commit()
        return {"status": 'success', 'message': 'Game is updated!'}

    def delete(self, id):
        game = game_model.query.filter_by(id=id).first()
        if not game:
            # Return a plain dictionary, no need to use jsonify
            return {"status": "failure", "message": "game not found!"}, 404

        # Proceed with deletion if the game is found
        db.session.delete(game)
        db.session.commit()

        # Return a success response as a plain dictionary
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
