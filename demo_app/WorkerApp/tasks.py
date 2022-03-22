from celery.schedules import crontab
from celery.utils.log import get_task_logger
from celery.task import periodic_task
from UserApp.models import update_post_count
from demo_app.celery import app

logger = get_task_logger(__name__)


@app.task(name="sum_two_numbers")
def add(x, y):
    logger.info(x)
    logger.info(y)
    return x + y


@periodic_task(name="update_post_count_task", run_every=crontab())
def update_post_count_task():
    update_post_count()


@periodic_task(name="test_task", run_every=crontab())
def test():
    print("hello")
