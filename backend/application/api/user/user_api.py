from application.data.database import db
from application.data.model import User as user_model
from flask_restx import Resource, fields, marshal, reqparse


genre_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'active': fields.Boolean,
    'fs_uniquifier': fields.String,
    'last_login_at': fields.DateTime,
    'current_login_at':fields.DateTime,
    'last_login_ip':fields.String,
    'current_login_ip':fields.String,
    'login_count':fields.Integer,
    'confirmed_at':fields.DateTime
    # This will be a list of genre titles
}

class AUserResource(Resource):
    def get(self):
        users = user_model.query.all()
        return {'status': 'success', 'users': marshal(users, genre_fields)}
    
class SUserResource(Resource):
    def get(self,id):
        user = user_model.query.get(id)
        if(not user):
            return {"message": 'User not found'}
        if(user.active):
            user.active = False
            print(user.active)
            db.session.commit()
            return {"status": 'success', 'message':'User Status is Deactivated'}
        else:
            user.active = True
            print(user.active) 
            db.session.commit() 
            return {"status": 'success', 'message':'User Status is Activated'} 
       