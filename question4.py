import json
import logging

from flask import Flask
from flask import request, jsonify, make_response
from flask_restful import Resource, Api, reqparse

from given import requestTask, checkTaskStatus, downloadData

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)

class TaskID(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('date_range', required=True, type=str, location='json',\
                                     help='date_range is required.')
        self.reqparse.add_argument('test_type', required=True, type=str, location='json',\
                                    help='test_type is required.')
        self.reqparse.add_argument('product', required=True, type=str, location='json',\
                                    help='product is required.')
    def post(self):
        args = self.reqparse.parse_args()
        date_range = args['date_range']
        test_type = args['test_type']
        product = args['product']
        try:
            taskid = requestTask(product, date_range, test_type)
        except Exception as e:
            return make_response(jsonify({'result': e}), 200)
        return make_response(jsonify({'result': taskid}), 200)
        
class TaskStatus(Resource):
    def get(self, task_id):
        try:
            task_ready = checkTaskStatus(task_id)
        except Exception as e:
            return make_response(jsonify({'result': e}), 200)
        return make_response(jsonify({'result': True}), 200)

class TriggerApp(Resource):
    def get(task_id):
        try:
            binary_encoded_string = downloadData(task_id)
        except Exception as e:
            return make_response(jsonify({'result': e}), 200)
        return make_response(jsonify({'result': binary_encoded_string}), 200)


# Processing data can be done on threads.
# Better way to handle threads is to run on Celery. Which uses Message queue. (Redis or RabbitMq)
# We can configure Nginx, Gunicorn and supervisord to get works and make sure server is up and running.
# Depends on data we can write to mysql or nosql.
# Schedule the job to get the data every 4 weeks and replace it with expired data.
