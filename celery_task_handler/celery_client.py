from celery import Celery

import settings
from errors import FailedToInsertTaskToCelery


class CeleryConfig(object):
    """
    Celery Clinet Configuration Class
    """
    CELERY_IGNORE_RESULTS = False
    BROKER_URL = settings.MQ_URL
    CELERY_RESULT_BACKEND = 'amqp'


app = Celery('myApp')
app.config_from_object(CeleryConfig)


def insert_task_to_mq(image_path):
    try:
        app.send_task(f'{settings.WORKER_NAME}.service.{settings.MQ_CMD}', args=[image_path])
    except Exception:
        raise FailedToInsertTaskToCelery
