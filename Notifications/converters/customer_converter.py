from Notifications.model.customer import Customer as cs
from Notifications.entities.customer import customers as ce

class converters:
    def customer_class_to_customer_entity(self,customer_class):
        c_to_ce=ce(id=customer_class.id,fname=customer_class.fname,lname=customer_class.lname,email=customer_class.email,favourite_templates=customer_class.favourite_templates,recepients=customer_class.recepients)
        return c_to_ce

    def customer_entity_to_customer_class(self,customer_enity):
        ce_to_c=cs(fname=customer_enity.fname,lname=customer_enity.lname,email=customer_enity.email,id=customer_enity.id,favourite_templates=customer_enity.favourite_templates,recepients=customer_enity.recepients)
        return ce_to_c

    def customer_entities_to_customers(self,customer_entities):
        ces_to_cs=[]
        if customer_entities !=None:
            for ces in customer_entities:
                ces_to_cs.append(self.customer_entity_to_customer_class(ces))
        return ces_to_cs