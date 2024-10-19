from application.api.auth.auth_api import LoginResource, RegisterResource
from application.api.game.game_api import (GameResource, SingleGameResource,
                                           TopGameListResource)
from application.api.game.genre_api import GenreResource, MultipleGenreResource
from flask_restx import Api

# ? id, title, genre, played


def initialize_api(app):
    api = Api(app)
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')
    api.add_resource(GameResource, '/api/games')
    api.add_resource(SingleGameResource, '/api/game/<int:id>')
    api.add_resource(TopGameListResource, '/api/games/top/<int:no>')
    api.add_resource(GenreResource, '/api/genre')
    api.add_resource(MultipleGenreResource, '/api/genre/<string:ids>')
    return api
