from datetime import datetime

from flask_restx import Resource, abort, fields, marshal, reqparse

from application import api  # your Api() instance
from application.data.database import db
from application.data.model import Profile as profile_model
from application.data.model import User as user_model

# 1) Define the output fields
profile_fields = {
    'id':           fields.Integer,
    'user_id':      fields.Integer,
    'username':     fields.String(attribute='user.username'),
    'email':        fields.String(attribute='user.email'),
    'first_name':   fields.String,
    'last_name':    fields.String,
    'gender':       fields.String,
    'date_of_birth': fields.String,  # ISO date
    'bio':          fields.String,
    'profile_picture': fields.String,
    'phone_number': fields.String,
    'address':      fields.String,
    'city':         fields.String,
    'state':        fields.String,
    'country':      fields.String,
    'postal_code':  fields.String,
    'github_url':   fields.String,
    'twitter_url':  fields.String,
    'linkedin_url': fields.String,
    'website_url':  fields.String,
    'created_at':   fields.DateTime(dt_format='iso8601'),
    'updated_at':   fields.DateTime(dt_format='iso8601'),
}

# 2) Define the parser for PUT / updates
profile_parser = reqparse.RequestParser()
profile_parser.add_argument('first_name',      type=str,   location='json')
profile_parser.add_argument('last_name',       type=str,   location='json')
profile_parser.add_argument('gender',          type=str,   location='json')
profile_parser.add_argument('date_of_birth',   type=str,   location='json',
                            help='YYYY-MM-DD')
profile_parser.add_argument('bio',             type=str,   location='json')
profile_parser.add_argument('profile_picture', type=str,   location='json')
profile_parser.add_argument('phone_number',    type=str,   location='json')
profile_parser.add_argument('address',         type=str,   location='json')
profile_parser.add_argument('city',            type=str,   location='json')
profile_parser.add_argument('state',           type=str,   location='json')
profile_parser.add_argument('country',         type=str,   location='json')
profile_parser.add_argument('postal_code',     type=str,   location='json')
profile_parser.add_argument('github_url',      type=str,   location='json')
profile_parser.add_argument('twitter_url',     type=str,   location='json')
profile_parser.add_argument('linkedin_url',    type=str,   location='json')
profile_parser.add_argument('website_url',     type=str,   location='json')


class ProfileResource(Resource):
    def get(self, userid):
        """Fetch the current user's profile"""
        try:
            profile = profile_model.query.filter_by(
                user_id=userid).first()
            if not profile:
                if not user_model.query.filter_by(id=userid).first():
                    abort(404, 'User not found')
                new_profie = profile_model(user_id=userid)
                db.session.add(new_profie)
                db.session.commit()
                profile = profile_model.query.filter_by(
                    user_id=userid).first()
            return {'status': 'success', 'profile': marshal(profile, profile_fields)}
        except:
            return {'status': 'success', 'profile': ""}

    def put(self, userid):
        """Update the current user's profile"""
        args = profile_parser.parse_args()
        profile = profile_model.query.filter_by(
            user_id=userid).first()
        if not profile:
            abort(404, 'Profile not found')
        for field, value in args.items():
            if value is None:
                continue
            if field == 'date_of_birth':
                try:
                    value = datetime.strptime(value, '%Y-%m-%d').date()
                except ValueError:
                    abort(400, 'Invalid date_of_birth format, expected YYYY-MM-DD')
            setattr(profile, field, value)

        db.session.commit()
        return {'status': 'success', 'profile': marshal(profile, profile_fields)}
