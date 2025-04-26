import logging
import os
from datetime import datetime, timedelta, timezone
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

from application.data.database import db
from application.data.model import Game as game_model
from application.data.model import Game_User as gu_model
from application.data.model import Review as review_model
from application.data.model import Subscription as sub_model
from application.data.model import User as user_model
from celery import shared_task
from flask import current_app as app
from jinja2 import Template


# Define a sample Celery task
@shared_task(ignore_result=False)
def async_task_example():
    print("Task executed asynchronously!")
    return "Task completed"


# from flask import current_app as app
current_timeutc = datetime.now(timezone.utc)
ist_offset = timedelta(hours=5, minutes=30)
current_time = current_timeutc + ist_offset


# Define a sample task
# @celery_app.task
# def async_task_example():
#     print("Task executed asynchronously!")
#     return "Task completed"


@shared_task(ignore_result=False)
def send_installer():
    try:
        static_folder = os.path.join(
            app.root_path, app.config['STATIC_FOLDER'])
        installer_path = os.path.join(static_folder, 'installer.zip')
        if os.path.exists(installer_path):
            with open(installer_path, 'rb') as f:
                zip_data = f.read()
            return zip_data
        else:
            return {"error": "installer.zip not found in static folder"}
    except Exception as e:
        return {"error": str(e)}


@shared_task(ignore_result=True)
def send_email(sender, reciever, subject, message, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = reciever
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'html'))
    filename = attachment
    if filename != '':
        path = os.path.join(os.getcwd(), filename)
        with open(path, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='pdf')
            attachment.add_header('Content-Disposition',
                                  'attachment', filename=filename)
            msg.attach(attachment)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = sender
    smtp_password = 'escp tovy kwcx bvcf'

    with SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, reciever, msg.as_string())
    return "MAIL SENT"


@shared_task(ignore_result=True)
def send_weekly_report_to_all_users():
    users = user_model.query.all()  # Fetch all users (excluding admin if needed)
    users = users[1:]  # Example: skipping the first user (admin)
    top_rated_games = game_model.query.order_by(
        game_model.rating.desc()).limit(5).all()
    top_rated_games_list = [{'game_id': game.id, 'title': game.title,
                             'rating': game.rating} for game in top_rated_games]
    for user in users:
        receiver = user.email
        subject = "Weekly Report | GameVault"

        # Prepare rented games information
        user_games = gu_model.query.filter_by(user_id=user.id).all()
        if user_games:
            rented_games = []
            for user_game in user_games:
                game = game_model.query.filter_by(id=user_game.game_id).first()
                if game:  # Check if the game exists
                    rented_games.append({
                        'game_title': game.title,
                        'purchased': user_game.purchased,
                        'subscribed': user_game.subscribed,
                        'completed': user_game.completed,
                        'date': user_game.purchase_date.strftime('%d/%m/%Y %H:%M') if user_game.purchase_date else 'N/A',
                    })

            data = {
                'user': user,
                'message': 'You have been playing the following games... Keep gaming!',
                'rented': rented_games,
                'top_rated_games': top_rated_games_list
            }
        else:
            data = {
                'user': user,
                'message': 'You have not played any games recently... Check out the latest games on GameVault!',
                'rented': [],
                'top_rated_games': top_rated_games_list
            }

        # Load template and generate the email content
        with open(app.config['TEMPLATES_PATH'] + '/weekly_report.html', 'r') as f:
            template = Template(f.read())
            rendered_message = template.render(data=data)

        # Send the email
        send_email.delay('manager.gamevault@gmail.com', receiver,
                         subject, rendered_message, '')


@shared_task(ignore_result=True)
def send_monthly_report_to_admin():
    # Get the first day of the current month
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)

    # Fetch data for report
    total_purchases = gu_model.query.filter_by(purchased=True).count()
    total_subscriptions = gu_model.query.filter_by(subscribed=True).count()

    # User-wise purchase/subscription analysis
    user_analysis = []
    users = user_model.query.all()
    for user in users:
        purchases = gu_model.query.filter_by(
            user_id=user.id, purchased=True).count()
        subscriptions = gu_model.query.filter_by(
            user_id=user.id, subscribed=True).count()
        user_analysis.append({
            'userid': user.id,
            'username': user.username,
            'purchases': purchases,
            'subscriptions': subscriptions,
        })

    # Genre-wise sales
    genre_sales = {}
    games = game_model.query.all()
    for game in games:
        genres = game.genres
        sales_count = gu_model.query.filter_by(
            game_id=game.id, purchased=True).count()
        for genre in genres:
            genre_sales[genre.title] = genre_sales.get(
                genre.title, 0) + sales_count

    # Newly added games (only from the current month)
    new_games = game_model.query.filter(
        game_model.release_date >= start_of_month).all()
    new_games_list = [{'game_id': game.id, 'title': game.title,
                       'release_date': game.release_date} for game in new_games]

    # Top rated games (Assuming rating system exists)
    top_rated_games = game_model.query.order_by(
        game_model.rating.desc()).limit(5).all()
    top_rated_games_list = [{'game_id': game.id, 'title': game.title,
                             'rating': game.rating} for game in top_rated_games]

    # User feedback (Assuming feedback system)
    user_feedback = []  # Populate with feedback data from database

    # Prepare data for template
    data = {
        'total_purchases': total_purchases,
        'total_subscriptions': total_subscriptions,
        'user_analysis': user_analysis,
        'genre_sales': genre_sales,
        'new_games': new_games_list,
        'top_rated_games': top_rated_games_list,
        'user_feedback': user_feedback
    }

    # Render the template
    with open('templates/monthly_report.html', 'r') as f:
        template = Template(f.read())
        rendered_message = template.render(data=data)

    # Send email
    send_email.delay('manager.gamevault@gmail.com', 'manager.gamevault@gmail.com',
                     'Monthly Report | GameVault', rendered_message, '')


@shared_task(ignore_result=True)
def autorevoke():
    with app.app_context():
        current_timeutc = datetime.now(timezone.utc)
        ist_offset = timedelta(hours=5, minutes=30)
        current_time = current_timeutc + ist_offset
        subs = sub_model.query.filter((sub_model.subscription_status == True) & (
            sub_model.subscription_end_date < current_time)).all()
        for i in subs:
            gus = gu_model.query.filter_by(user_id=i.userid).all()
            for j in gus:
                j.subscribed = False
            i.status = False
            db.session.commit()
        db.session.commit()
        return 'AUTO REVOKE DONE'


@shared_task(ignore_result=True)
def ratingcal():
    with app.app_context():
        games = game_model.query.all()
        for i in games:
            rats = review_model.query.filter_by(game_id=i.id).all()
            if len(rats) != 0:
                av = 0.0
                sum, c = 0, 0
                for j in rats:
                    av2 = 0.0
                    sum += j.rating
                    c += 1
                    av = sum/c
                    av2 = round(av, 2)
                i.rating = av2
            db.session.commit()
        db.session.commit()
        return 'RATING UPDATED'
