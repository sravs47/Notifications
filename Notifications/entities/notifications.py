from Notifications.models import db
from sqlalchemy import ForeignKey,func
class notifications(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    template_name = db.Column('template_name',db.String(40),ForeignKey("templates.name"))
    sender = db.Column('sender',db.String(30))
    cc=db.Column('cc',db.String(30))
    bcc=db.Column('bcc',db.String(30))
    subject=db.Column('subject',db.String(30))
    created_date = db.Column('created_date',db.DateTime,default=func.sysdate())
    status = db.Column('status',db.String(10))

    def __init__(self,template_name,sender,cc,bcc,subject,created_date,status):
        self.template_name=template_name
        self.sender=sender
        self.cc=cc
        self.bcc=bcc
        self.subject=subject
        self.status=status



