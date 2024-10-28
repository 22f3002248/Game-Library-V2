from application.api.auth.auth_api import LoginResource, RegisterResource
from application.api.game.game_api import (GamePhotoResource, GameResource,
                                           SingleGameResource,
                                           TopGameListResource)
from application.api.game.genre_api import (AGenreResource,
                                            AMultipleGenreResource,
                                            ASingleGenreResource)
from application.api.genre.genre_api import (GenreResource,
                                             MultipleGenreResource)
from application.api.purchase.purchase_api import (CheckPurchase,
                                                   GetAllPurchasedResource,
                                                   GetPurchasedResource,
                                                   PurchaseResource)
from application.api.purchase.subscription_api import (CheckSubscription,
                                                       SubscriptionResource)
from application.api.reviews.review_api import (ModifyReviewResource,
                                                ReviewResource)
from flask_restx import Api


def initialize_api(app):
    api = Api(app)
    # > AUTH
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')
    # > GAME/GENRE APIs
    api.add_resource(GameResource, '/api/games')
    api.add_resource(GenreResource, '/api/genre')
    api.add_resource(SingleGameResource, '/api/game/<int:id>')
    api.add_resource(GamePhotoResource, '/api/game/<int:gameid>/photos')
    api.add_resource(TopGameListResource, '/api/games/top/<int:no>')
    api.add_resource(GenreResource, '/api/genre')
    api.add_resource(MultipleGenreResource, '/api/genre/<string:ids>')
    # > PURCHASE/SUBSCRIPTION APIs
    api.add_resource(
        CheckPurchase, '/api/check/purchase/<int:userid>/<int:gameid>')
    api.add_resource(PurchaseResource,
                     '/api/purchase/<int:userid>/<int:gameid>')
    api.add_resource(GetPurchasedResource,
                     '/api/purchase/<int:userid>/purchased')
    api.add_resource(GetAllPurchasedResource,
                     '/api/purchase/<int:userid>/purchased/all')
    api.add_resource(CheckSubscription, '/api/check/subscription/<int:userid>')
    api.add_resource(SubscriptionResource, '/api/subscribe/<int:userid>')

    # > REVIEW
    api.add_resource(
        ReviewResource, '/api/review/<int:gameid>')
    api.add_resource(ModifyReviewResource,
                     '/api/review/modify/<int:userid>/<int:gameid>')

    # admin
    api.add_resource(AGenreResource, '/admin/genre')
    api.add_resource(AMultipleGenreResource, '/admin/genre/<string:ids>')
    api.add_resource(ASingleGenreResource, '/admin/genre/<int:id>')
    api.add_resource(GameResource, '/admin/games')
    api.add_resource(SingleGameResource, '/admin/games/<int:id>')
    return api
