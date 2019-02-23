from Notifications.models import db

class customers(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    fname = db.Column('fname',db.String(20))
    lname = db.Column('lname',db.String(20))
    email = db.Column('email',db.String(40))
    favourite_templates = db.Column('favourite_templates',db.String(100))
    recepients = db.Column('recepients',db.String(300))

    def __init__(self,fname,lname,email,favourite_templates,recepients):
        self.fname=fname
        self.lname=lname
        self.email = email
        self.favourite_templates=favourite_templates
        self.recepients=recepients

