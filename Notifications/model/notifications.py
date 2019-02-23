class notifications:
    def __init__(self,template_name,sender,cc,bcc,subject,created_date,status,id=None):
        self.template_name=template_name
        self.sender=sender
        self.cc=cc
        self.bcc=bcc
        self.subject=subject
        self.created_date=created_date
        self.status=status
        self.id=id
        
