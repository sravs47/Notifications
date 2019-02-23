from Notifications.model.templates import Templates
from Notifications.entities.templates import templates as templates_entity

class templates_converters:

    def template_to_template_entity(self,template_class):
        t_to_te=templates_entity(id=template_class.id,name=template_class.name,occasion=template_class.occasion,author=template_class.author,header=template_class.header,body=template_class.body,footer=template_class.footer,image=template_class.image)
        return t_to_te

    def template_entity_to_template(self,template_entity):
        te_to_t = Templates(name=template_entity.name,occasion=template_entity.occasion,author=template_entity.author,header=template_entity.header,body=template_entity.body,footer=template_entity.footer,id=template_entity.id,image=template_entity.image)
        return te_to_t

    def template_entities_to_templates(self,template_entities):
        tes_to_t = []
        if template_entities !=None:
            for tes in template_entities:
                tes_to_t.append(self.template_entity_to_template(tes))
        return tes_to_t
