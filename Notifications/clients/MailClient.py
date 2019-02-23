import smtplib


class mail_client:
    def __init__(self,sender,recepeints_list,message,subject):
        self.sender=sender
        self.recepients=recepeints_list
        self.message=message
        self.subject=subject

    def send_mail(self):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login('sravanims2017@gmail.com', 'micromax')
            server.sendmail(self.sender, self.recepients,self.message)
            server.close()
            print
            'successfully sent the mail'
        except:
            print
            "failed to send mail"

