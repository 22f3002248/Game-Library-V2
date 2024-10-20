from application.api.initialize_api import initialize_api
from application.data.database import db
from application.data.datastore import ds
from config import devconfig
from datagen import create_games, create_genres, gen
from flask import Flask, current_app
from flask_cors import CORS
from flask_security import Security


def create_app():
    app = Flask(__name__)
    app.config.from_object(devconfig)
    CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    security = Security(app, ds)
    api = initialize_api(app)
    with app.app_context():
        db.create_all()
        gen()
        create_genres()
        create_games()

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        app.run(debug=True)
