
from flask import Flask
from flask_restful import Api
from Notifications.resources.customer_catalog import cus_blueprint
from Notifications.resources.templates_catalog import template_blueprint
from Notifications.resources.notifications_catalog import not_blueprint
app = Flask(__name__)
api = Api(cus_blueprint,template_blueprint)
from Notifications.models import db
from Notifications.entities import customer
from Notifications.manage import migrate
from Notifications.resources import customer_catalog
from Notifications.resources.customer_catalog import cr_customers,ud_customers
from Notifications.resources.templates_catalog import cr_template,ud_template
import logging

POSTGRES ={
    'user':'postgres',
    'pw':'123123',
    'db':'notifications',
    'host':'localhost',
    'port':'5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('logs/customer_catalog.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


db.init_app(app)

app.register_blueprint(cus_blueprint)
app.register_blueprint(template_blueprint)
app.register_blueprint(not_blueprint)

api.add_resource(cr_customers,'/customers')
api.add_resource(ud_customers,'/customers/<customer_id>')
api.add_resource(cr_template,'/templates')
api.add_resource(ud_template,'/templates/<temp_id>')
name = "Notifications"


if __name__ == '__main__':
    app.run(host='localhost',debug=True)