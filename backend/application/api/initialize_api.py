from application.api.auth.auth_api import LoginResource, RegisterResource
from application.api.game.game_api import GameResource, SingleGameResource
from application.api.game.genre_api import GenreResource
from flask_restx import Api

# ? id, title, genre, played


def initialize_api(app):
    api = Api(app)
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')
    api.add_resource(GameResource, '/games')
    api.add_resource(SingleGameResource, '/games/<int:id>')
    api.add_resource(GenreResource, '/genre')
    return api
