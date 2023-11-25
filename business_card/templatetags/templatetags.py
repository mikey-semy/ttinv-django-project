from django import template
import business_card.views as views


register = template.Library()


@register.inclusion_tag('business_card/partials/caption.html')
def caption(section_name):
    captions = views.captions
    return {'caption': captions[section_name]}
