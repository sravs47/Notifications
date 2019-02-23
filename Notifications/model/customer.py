class Customer:
    def __init__(self,fname,lname,email,id=None,favourite_templates=None,recepients=None):
        self.id =id
        self.fname=fname
        self.lname=lname
        self.email=email
        self.favourite_templates=favourite_templates
        self.recepients=recepients

