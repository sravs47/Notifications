from flask_restful import Resource
import json
from flask import request,Response,Blueprint
from Notifications.utils import to_dict,JSON_MIME_TYPE
not_blueprint = Blueprint('not_blueprint',__name__)
from Notifications.db_operations.notifications import notification_middleware
from Notifications.model.notifications import notifications

noti_blueprint = Blueprint('noti_blueprint',__name__)


class notification_catalog(Resource):
    def get(self):
        notification_data = notification_middleware().get_notification()
        return Response(json.dumps(to_dict(notification_data)),status=200,mimetype=JSON_MIME_TYPE)

    def post(self):
        data = request.json
        to_model=notifications(data['template_name'],data['sender'],data['cc'],data['bcc'],data['subject'],data['created_date'],data['status'],data['id'])


