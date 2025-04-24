from application.api.initialize_api import initialize_api
from application.data.database import db
from application.data.datastore import ds
from application.tasks import (async_task_example, autorevoke, ratingcal,
                               send_email, send_installer,
                               send_monthly_report_to_admin,
                               send_weekly_report_to_all_users)
from application.worker import celery_init_app
from celery.result import AsyncResult
from celery.schedules import crontab
from config import devconfig
from datagen import (assign_games_to_users, create_game_photos, create_games,
                     create_genres, gen, gen_reviews)
from flask import Flask, jsonify, send_file
from flask_cors import CORS
from flask_security import Security

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
    assign_games_to_users()
    gen_reviews()
    create_game_photos()


@app.route('/run-simple-task')
def simple_task():
    res = async_task_example.delay()
    return jsonify({'task_id': res.id})


@app.route('/download-installer')
def installer_task():
    res = send_installer.delay()
    return jsonify({'task_id': res.id})


@app.route('/result-download-installer/<task_id>')
def installer_task_result(task_id):
    res = AsyncResult(task_id)
    if res.ready():
        filename = res.result
        return send_file(filename, as_attachment=True)
    else:
        return jsonify({"message": "Task is pending !"}), 404


celery_app = celery_init_app(app)


@celery_app.on_after_configure.connect
def celery_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=10, minute=29),
        send_weekly_report_to_all_users.s(),
    )
    sender.add_periodic_task(
        crontab(hour=10, minute=29),
        send_monthly_report_to_admin.s(),
    )
    sender.add_periodic_task(
        crontab(minute='*/10'),
        autorevoke.s(),
    )
    sender.add_periodic_task(
        crontab(minute='*/10'),
        ratingcal.s(),
    )
    # autorevoke.apply_async()
    # ratingcal.apply_async()


if __name__ == "__main__":
    app.run(debug=True)
