from Notifications.model.notifications import notifications as notifications_model
from Notifications.entities.notifications import notifications as notifications_entity

class notifications_converter:
    def noti_entity_to_noti_class(self,noti_entity):
        ne_to_nc = notifications_model(template_name=noti_entity.template_name,sender=noti_entity.sender,cc=noti_entity.cc,bcc=noti_entity.bcc,subject=noti_entity.subject,created_date=noti_entity.created_date,status=noti_entity.status)
        return ne_to_nc