from datetime import datetime, timedelta, timezone

from flask_restx import Resource, abort, fields, marshal, reqparse

from application.api.game.genre_api import genre_fields
from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import GamePhoto as game_photos_model
from application.data.model import Genre as genre_model
from application.data.model import Review as review_model
from application.data.model import User as user_model

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
    'played': fields.Boolean,
    'poster': fields.String(attribute=lambda x: x.get_cover_image())
}


# Define the fields for the Game review
review_fields = {
    'id': fields.Integer,
    'user_id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'game_id': fields.Integer,
    'title': fields.String,
    'rating': fields.Integer,
    'feedback': fields.String,
    'date': fields.String
}


games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'title', type=str, required=True, help="Title is required!"
)
games_parser.add_argument(
    'genre_ids', type=int, action='append', help="Genres must be provided as a list of genre IDs!"
)
games_parser.add_argument(
    'played', type=bool, default=False, help="Played can be given optionally!"
)

# Define the parser for the POST request
review_parser = reqparse.RequestParser()
review_parser.add_argument(
    'user_id', type=int, required=True, help='User ID is required')
review_parser.add_argument(
    'game_id', type=int, required=True, help='Game ID is required')
review_parser.add_argument('rating', type=int, required=True,
                           help='Rating is required and should be an integer')
review_parser.add_argument(
    'feedback', type=str, help='Feedback is required')


def current_time():
    current_timeutc = datetime.now(timezone.utc)
    ist_offset = timedelta(hours=5, minutes=30)
    current_time = current_timeutc + ist_offset
    return current_time


class ReviewResource(Resource):
    def get(self, gameid):
        reviews = review_model.query.filter_by(game_id=gameid).all()
        if not reviews:
            return {'status': 'failure', 'message': 'Review not found'}, 404

        # Get the related user and game details
        review_data = []
        for review in reviews:
            review_data.append({
                'id': review.id,
                'user_id': review.user_id,
                'username': review.user.username,
                'email': review.user.email,
                'game_id': review.game_id,
                'title': review.game.title,
                'rating': review.rating,
                'feedback': review.feedback,
                'date': review.date
            })

        return {'status': 'success', 'reviews': marshal(review_data, review_fields)}

    def post(self, gameid):
        args = review_parser.parse_args()
        user = user_model.query.filter_by(id=args['user_id']).first()
        if not user:
            abort(404, message="User not found")
        game = game_model.query.filter_by(id=args['game_id']).first()
        if not game:
            abort(404, message="Game not found")
        new_review = review_model(
            user_id=args.get('user_id'),
            game_id=args.get('game_id'),
            rating=args.get('rating'),
            feedback=args.get('feedback'),
            date=current_time()
        )
        db.session.add(new_review)
        db.session.commit()
        review_data = {
            'id': new_review.id,
            'user_id': new_review.user_id,
            'username': user.username,
            'email': user.email,
            'game_id': new_review.game_id,
            'title': game.title,
            'rating': new_review.rating,
            'feedback': new_review.feedback,
            'date': new_review.date
        }
        return {'status': 'success', 'message': 'Review created successfully', 'reviews': marshal(review_data, review_fields)}, 201


class ModifyReviewResource(Resource):
    def get(self, userid, gameid):
        review = review_model.query.filter_by(
            user_id=userid, game_id=gameid).first()
        if not review:
            return {'status': 'failure', 'message': 'Review not found'}, 404
        review_data = {
            'id': review.id,
            'user_id': review.user_id,
            'username': review.user.username,
            'email': review.user.email,
            'game_id': review.game_id,
            'title': review.game.title,
            'rating': review.rating,
            'feedback': review.feedback,
            'date': review.date
        }

        return {'status': 'success', 'review': marshal(review_data, review_fields)}

    def delete(self, userid, gameid):
        review = review_model.query.filter_by(
            user_id=userid, game_id=gameid).first()
        if review:
            db.session.delete(review)
            db.session.commit()
            return {'status': 'success', 'message': 'Review deleted !'}
        else:
            return {'status': 'failure', 'message': 'Review not found !'}

    def put(self, userid, gameid):
        args = review_parser.parse_args()
        review = review_model.query.filter_by(
            user_id=userid, game_id=gameid).first()
        if review is not None:
            if args.get('rating') is not None:
                review.rating = args.get('rating')
            if args.get('feedback') is not None:
                review.feedback = args.get('feedback')
            review.date = current_time()

            db.session.commit()
            return {'status': 'success', 'message': 'Review updated !'}
        else:
            return {'status': 'failure', 'message': 'Review not found !'}


class AdminReviewResource(Resource):
    def get(self):
        reviews = review_model.query.all()
        if not reviews:
            return {'status': 'failure', 'message': 'Review not found'}, 404

        # Get the related user and game details
        review_data = []
        for review in reviews:
            review_data.append({
                'id': review.id,
                'user_id': review.user_id,
                'username': review.user.username,
                'email': review.user.email,
                'game_id': review.game_id,
                'title': review.game.title,
                'rating': review.rating,
                'feedback': review.feedback,
                'date': review.date
            })

        return {'status': 'success', 'message': 'reviews load successfully', 'reviews': marshal(review_data, review_fields)}, 200
