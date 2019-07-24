import os

from flask import request
from flask_restful_swagger_2 import swagger, Resource
from magic import Magic

import settings
from api_resources.models import ErrorModel, ResponseModel
from celery_task_handler.celery_client import insert_task_to_mq


class ResizeVideoFramesResource(Resource):
    @swagger.doc({
        'tags': ['resize_video_frames'],
        'description': 'Resize Video Frames',
        'parameters': [
            {
                'name': 'image',
                'description': 'image File',
                'in': 'formData',
                'type': 'file',
                'required': True,
            }],
        'responses': {
            '200': {
                'description': 'All the frames of the video was successfully resize',
                'schema': ResponseModel,
                'headers': {
                    'Location': {
                        'type': 'string',
                        'description': ''
                    }
                },
                'examples': {
                    'application/json': {
                    },
                }
            }
        }
    })
    def post(self):
        """
        Resize video frames
        """
        # Validate request body with schema model
        try:
            image_file = request.files['image']
            imgae_path = fr'{settings.IMAGE_PATH}\{image_file.filename}'
            image_file.save(imgae_path)
            mime = Magic(mime=True)
            filename = mime.from_file(imgae_path)
            if 'image' not in filename:
                os.remove(imgae_path)
                return ErrorModel(**{'message': 'Not A Valid Image File'}), 400
            insert_task_to_mq(imgae_path)
        except ValueError as e:
            return ErrorModel(**{'message': e.args[0]}), 400
        return ResponseModel(**{'message': 'yey'}), 200
