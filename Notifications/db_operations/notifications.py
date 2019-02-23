from Notifications.entities.notifications import notifications as notifications_entity
from Notifications.model.notifications import notifications as notifications_class
from Notifications.models import db
from Notifications.converters.notification_converter import notifications_converter


class notification_middleware:
    def get_notification(self,not_id):
        data = notifications_entity.query.filter(notifications_entity.id==not_id)
        return notifications_converter().noti_entity_to_noti_class(data)

    def add_notifications(self,notification):
        data = notifications_entity(template_name=notification.template_name,sender=notification.sender,cc=notification.cc,bcc=notification.bcc,status=notification.status)
        db.session.add(data)
        db.session.commit()
        return self.get_notification(notification.id)



