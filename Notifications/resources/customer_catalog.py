import json
from flask import request,Response,Blueprint
from Notifications.model.customer import Customer
#from Notifications import api
from flask_restful import Resource
from Notifications.utils import to_dict,JSON_MIME_TYPE
from Notifications.db_operations.customers import customers_middleware
from logging import getLogger as logger

cus_blueprint = Blueprint('cus_blueprint',__name__)


class cr_customers(Resource):
    def get(self):
        all_customers=[]
        customer_data =customers_middleware().get_customers()
        for cust in customer_data:
            all_customers.append(to_dict(cust))
        return Response(json.dumps(all_customers),status = 200,mimetype=JSON_MIME_TYPE)


    def post(self):
        data = request.json
        customer = Customer(data['fname'],data['lname'],data['email'],data['id'],data['favourite_templates'],data['recepients'])
        cust_data =customers_middleware().add_customers(customer)
        return Response(json.dumps(to_dict(cust_data)),status=201,mimetype=JSON_MIME_TYPE)


class ud_customers(Resource):
    def put(self,customer_id):
        data = request.json
        customer = Customer(data['fname'],data['lname'],data['email'],data['id'],data['favourite_templates'],data['recepients'])
        cust_data=customers_middleware().update_customer(customer,customer_id)
        return Response(json.dumps(to_dict(cust_data)),status=201,mimetype=JSON_MIME_TYPE)

    def delete(self,customer_id):
        customers_middleware().delete_customer(customer_id)
        return Response(status=202,mimetype=JSON_MIME_TYPE)




