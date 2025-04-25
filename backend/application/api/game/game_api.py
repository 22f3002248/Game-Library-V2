import os
from datetime import datetime

from application.api.game.genre_api import genre_fields
from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import GamePhoto as game_photos_model
from application.data.model import Genre as genre_model
from flask import current_app as app
from flask import request
from flask_restx import Resource, fields, marshal, reqparse

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
    'description', type=str, required=True, help="description is required!"
)
games_parser.add_argument(
    'price', type=float, required=True, help="price is required!"
)
games_parser.add_argument(
    'multiplayer', type=bool, required=True, help="multiplayer value is required!"
)

class GameResource(Resource):
    # ? to send all the games
    def get(self):
        games = game_model.query.all()
        genres = genre_model.query.all()
        return {'status': 'success', 'games': marshal(games, game_fields), 'genres': marshal(genres, genre_fields)}

    def post(self):
        args = games_parser.parse_args()
        title = args['title']

        if title:
            new_game = game_model(
                title=title,
                release_date=args['release_date'],
                developer=args['developer'],
                publisher=args['publisher'],
                platform=args['platform'],
                description=args['description'],
                price=args['price'],
                multiplayer=args['multiplayer'],
            )

        release_date = args['release_date']
        if isinstance(release_date, str):
            new_game.release_date = datetime.strptime(
                release_date, '%Y-%m-%d').date()

        genre_ids = args.get('genre_ids', [])
        if genre_ids:
            genres = genre_model.query.filter(
                genre_model.id.in_(genre_ids)).all()
            new_game.genres = genres

        db.session.add(new_game)
        db.session.commit()

        print(f"New game ID: {new_game.id}")

        # File handling
        file = request.files.get('poster')
        print(file)
        if file:
            if file.filename == '':
                return {'message': 'No selected file'}, 400

            # Extract the file extension
            file_extension = file.filename.rsplit(
                '.', 1)[1].lower() if '.' in file.filename else ''

            # Generate the new file name using the game ID and extension
            new_filename = f"{new_game.id}.{file_extension}"
            print(f"Saving file as: {new_filename}")

            # Save the file in the specified location
            file.save(os.path.join(
                app.root_path, app.config['STATIC_FOLDER'], 'game_posters', new_filename))

            return {'status': 'success', 'message': 'Game and poster added successfully!'}
        else:
            return {'status': 'success', 'message': 'Game added without poster!'}


class SingleGameResource(Resource):
    # ? to send all the games
    def get(self, id):
        games = game_model.query.filter_by(id=id).first()
        return {'status': 'success', 'game': marshal(games, game_fields)}

    def put(self, id):
        args = games_parser.parse_args()
        game = game_model.query.filter_by(id=id).first()
        if not game:
            return {"status": 'failure', 'message': 'game not found !'}, 404

        if args.get('title'):
            game.title = args['title']
            game.developer = args['developer']
            game.publisher = args['publisher']
            game.platform = args['platform']
            game.description = args['description']
            game.price = args['price']
            game.multiplayer = args['multiplayer']

        if args['release_date']:
            release_date = args['release_date']
            if isinstance(release_date, str):
                game.release_date = datetime.strptime(
                    release_date, '%Y-%m-%d').date()
                
        genre_ids = args.get('genre_ids', [])
        if genre_ids:
            genres = genre_model.query.filter(
                genre_model.id.in_(genre_ids)).all()
            game.genres = genres  # Associate new genres

        # file handling

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


class GamePhotoResource(Resource):
    def get(self, gameid):
        gps = game_photos_model.query.filter_by(game_id=gameid).first()
        if gps:
            pic_res = []
            if gps.picture1 != None:
                pic_res.append(gps.picture1)
            if gps.picture2 != None:
                pic_res.append(gps.picture2)
            if gps.picture3 != None:
                pic_res.append(gps.picture3)
            if gps.picture4 != None:
                pic_res.append(gps.picture4)
            if gps.picture5 != None:
                pic_res.append(gps.picture5)
            return {"status": "success", "photos": pic_res}
