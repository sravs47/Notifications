from Notifications.models import db
class templates(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(20))
    occasion = db.Column('occasion',db.String(20))
    author=db.Column('author',db.String(20))
    header=db.Column('header',db.String(100))
    body = db.Column('body', db.String(200))
    footer = db.Column('footer', db.String(100))
    image = db.Column('image',db.String(10))

    def __init__(self,id,name,occasion,author,header,body,footer,image):
        self.id=id
        self.name=name
        self.occasion=occasion
        self.author=author
        self.header=header
        self.body=body
        self.footer=footer
        self.image=image
