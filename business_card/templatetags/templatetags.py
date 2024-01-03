from django import template
import business_card.views as views
from business_card.models import Delivery

register = template.Library()


@register.inclusion_tag('business_card/partials/caption.html')
def caption(section_name):
    captions = views.captions
    return {'caption': captions[section_name]}


@register.inclusion_tag('business_card/partials/nav.html')
def navigation(type_nav, links_nav):
    nav = views.nav
    return {'type_nav': type_nav, 'nav': nav[links_nav]}

@register.inclusion_tag('business_card/partials/dialog.html')
def dialog(name_dialog):
    dialog_model = Delivery.objects.filter(name=name_dialog)
    return {'name_dialog': name_dialog, 'dialog': dialog_model}
