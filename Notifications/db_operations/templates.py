from Notifications.entities.templates import templates
from Notifications.models import db
from Notifications.converters.templates_converter import templates_converters

class template_middleware:
    def get_templates(self):
        templates_data=templates.query.all()
        x=templates_data
        return templates_converters().template_entities_to_templates(templates_data)

    def add_templates(self,template):
        data =templates(id=template.id,name=template.name,occasion=template.occasion,author=template.author,header=template.header,body=template.body,footer=template.footer,image=template.image)
        db.session.add(data)
        db.session.commit()
        return self.get_template(template.id)

    def get_template(self,template_id):
        temp_data = templates.query.filter(templates.id==template_id).first()
        print("----------------------output in get_templates")
        print(temp_data)
        return templates_converters().template_entity_to_template(temp_data)

    def update_template(self,template,temp_id):
        print("Template id in update_template")
        print(temp_id)
        print(template.id)
        if temp_id==template.id:
            temp_data = templates.query.filter(templates.id==template.id).first()
            if temp_data is not None:
                temp_data.name=template.name
                temp_data.occasion=template.occasion
                temp_data.author=template.author
                temp_data.header=template.header
                temp_data.body=template.body
                temp_data.footer=template.footer
                temp_data.image=template.image
            db.session.add(temp_data)
            db.session.commit()
            return self.get_template(template.id)

    def delete_template(self,temp_id):
        temp_data = templates.query.filter(templates.id==temp_id).first()
        if temp_data is not None:
            templates.query.filter_by(id=temp_id).delete()
            db.session.commit()

