from flask_restx import Api

from application.api.auth.auth_api import LoginResource, RegisterResource
from application.api.game.game_api import (CompleteGameListResource,
                                           GamePhotoResource, GameResource,
                                           SingleGameResource,
                                           TopGameListResource)
from application.api.game.genre_api import (AGenreResource,
                                            AMultipleGenreResource,
                                            ASingleGenreResource)
from application.api.genre.genre_api import (GenreResource,
                                             MultipleGenreResource)
from application.api.profile.profile_api import ProfileResource
from application.api.purchase.purchase_api import (CheckPurchase,
                                                   GetAllPurchasedResource,
                                                   GetPurchasedResource,
                                                   PurchaseResource)
from application.api.purchase.subscription_api import (CheckSubscription,
                                                       GetHash,
                                                       GetSubscribedGames,
                                                       SubscriptionResource)
from application.api.reviews.review_api import (AdminReviewResource,
                                                ModifyReviewResource,
                                                ReviewResource)
from application.api.stats.stat import UserStats
from application.api.user.user_api import AUserResource, SUserResource


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
    api.add_resource(CompleteGameListResource,
                     '/api/games/completed/<int:userid>')

    # > PURCHASE/SUBSCRIPTION APIs
    api.add_resource(
        CheckPurchase, '/api/check/purchase/<int:userid>/<int:gameid>')
    api.add_resource(PurchaseResource,
                     '/api/purchase/<int:userid>/<int:gameid>')
    api.add_resource(GetPurchasedResource,
                     '/api/purchase/<int:uid>/purchased')
    api.add_resource(GetAllPurchasedResource,
                     '/api/purchase/<int:userid>/purchased/all')
    api.add_resource(CheckSubscription, '/api/check/subscription/<int:userid>')
    api.add_resource(SubscriptionResource, '/api/subscribe/<int:userid>')
    api.add_resource(GetSubscribedGames,
                     '/api/subscription/<int:userid>/games')
    # > REVIEW
    api.add_resource(
        ReviewResource, '/api/review/<int:gameid>')
    api.add_resource(ModifyReviewResource,
                     '/api/review/modify/<int:userid>/<int:gameid>')
    api.add_resource(ProfileResource, '/api/user/<int:userid>/profile')
    api.add_resource(UserStats, '/api/user/stats/<int:userid>')
    # admin
    api.add_resource(AGenreResource, '/admin/genre')
    api.add_resource(AMultipleGenreResource, '/admin/genre/<string:ids>')
    api.add_resource(ASingleGenreResource, '/admin/genre/<int:id>')
    api.add_resource(GameResource, '/admin/games')
    api.add_resource(SingleGameResource, '/admin/games/<int:id>')
    api.add_resource(AUserResource, '/admin/users')
    api.add_resource(GetHash, '/api/user/<int:userid>/game/<int:gameid>/hash')
    api.add_resource(SUserResource, '/admin/users/<int:id>')
    api.add_resource(AdminReviewResource, '/admin/reviews')
    return api
