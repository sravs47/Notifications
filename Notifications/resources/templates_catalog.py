import json
from flask import request,Response,Blueprint
from flask_restful import Resource
from Notifications.utils import to_dict,JSON_MIME_TYPE
from Notifications.db_operations.templates import template_middleware
from Notifications.model.templates import Templates

template_blueprint = Blueprint('template_blueprint',__name__)

class cr_template(Resource):
    def get(self):
        all_templates=[]
        templates = template_middleware().get_templates()
        for temp in templates:
            all_templates.append(to_dict(temp))
        return Response(json.dumps(all_templates),status=200,mimetype=JSON_MIME_TYPE)

    def post(self):
        data = request.json
        template = Templates(data['name'],data['occasion'],data['author'],data['header'],data['body'],data['footer'],data['id'],data['image'])
        temp_data =template_middleware().add_templates(template)
        return Response(json.dumps(to_dict(temp_data)),status=201,mimetype=JSON_MIME_TYPE)


class ud_template(Resource):
    def put(self,temp_id):
        data = request.json
        template = Templates(data['name'],data['occasion'],data['author'],data['header'],data['body'],data['footer'],data['id'],data['image'])
        print(temp_id)
        print(template)
        temp_data = template_middleware().update_template(template,temp_id)
        print("-------------------")
        print(temp_data)
        return Response(json.dumps(to_dict(temp_data)),status=201,mimetype=JSON_MIME_TYPE)


    def delete(self,temp_id):
        template_middleware().delete_template(temp_id)
        return Response(status=202,mimetype=JSON_MIME_TYPE)

