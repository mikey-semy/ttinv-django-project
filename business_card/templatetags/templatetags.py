from django import template
import business_card.views as views
from business_card.models import Deliveries, Catalogs, Groups
from django.template.defaultfilters import register
register = template.Library()


@register.inclusion_tag('business_card/partials/caption.html')
def caption(section_name):
    captions = views.captions
    return {'caption': captions[section_name]}

@register.inclusion_tag('business_card/partials/nav.html')
def navigation(type_nav, links_nav):
    nav = views.nav

    return {'type_nav': type_nav, 'nav': nav[links_nav], 'page': links_nav}

@register.inclusion_tag('business_card/partials/dialog.html')
def dialog(name_dialog):
    dialog_model = Deliveries.objects.filter(name=name_dialog)
    return {'name_dialog': name_dialog, 'dialog': dialog_model}

# @register.inclusion_tag('business_card/partials/catalog.html')
# def catalog(name_group):
#     # catalog = Catalog.objects.get(pk=1)
#     return {'name_group': name_group, 'catalog': catalog}


@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]