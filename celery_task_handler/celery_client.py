from celery import Celery
from celery.result import allow_join_result

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
        with allow_join_result():
            return app.send_task('resize_frames_worker.service.resize_videos_frames_report', args=[image_path]).get()
    except Exception:
        raise FailedToInsertTaskToCelery
