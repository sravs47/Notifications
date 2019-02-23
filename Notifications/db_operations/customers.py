from Notifications.entities.customer import customers
from Notifications.converters.customer_converter import converters
from Notifications.models import db


class customers_middleware:
    def get_customers(self):
        customer_data = customers.query.all()
        x=customer_data
        return converters().customer_entities_to_customers(customer_data)

    def add_customers(self,customer):
        data = customers(id=customer.id,fname=customer.fname,lname=customer.lname,email=customer.email,favourite_templates=customer.favourite_templates,recepients=customer.recepients)
        y = db.session.add(data)
        db.session.commit()
        return self.get_customer(customer.id)

    def get_customer(self,customer_id):
        customer_data = customers.query.filter(customers.id==customer_id).first()
        return converters().customer_entity_to_customer_class(customer_data)

    def update_customer(self,customer,cust_id):
        if cust_id==customer.id :
            customer_data = customers.query.filter(customers.id==customer.id).first()
            if customer_data is not None:
                customer_data.id=customer.id
                customer_data.fname=customer.fname
                customer_data.lname=customer.lname
                customer_data.favourite_templates=customer.favourite_templates
                customer_data.recepients=customer.recepients
            db.session.add(customer_data)
            db.session.commit()
            return self.get_customer(customer.id)

    def delete_customer(self,customer_id):
        customer_data = customers.query.filter(customers.id==customer_id).first()
        if customer_data is not None:
            x = customers.query.filter_by(id=customer_id).delete()
            db.session.commit()








