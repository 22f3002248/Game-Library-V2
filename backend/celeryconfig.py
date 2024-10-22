from celery.schedules import crontab
broker_url = "redis://localhost:6379/1"
result_backend = "redis://localhost:6379/2"
timezone = 'Asia/Kolkata'

broker_connection_retry_on_startup = True

CELERY_BEAT_SCHEDULE = {
    'send-weekly-report': {
        'task': 'application.tasks.send_weekly_report_to_all_users',
        'schedule': crontab(hour=9, minute=2),
    },
    'send-monthly-report': {
        'task': 'application.tasks.send_monthly_report_to_admin',
        'schedule': crontab(hour=9, minute=2),
    },
    'autorevoke-task': {
        'task': 'application.tasks.autorevoke',
        'schedule': crontab(minute='*/1'),
    },
    'ratingcal-task': {
        'task': 'application.tasks.ratingcal',
        'schedule': crontab(minute='*/1'),
    }
}
