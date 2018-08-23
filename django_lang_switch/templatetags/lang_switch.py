"""Language switch template tags."""
from django import template

register = template.Library()


@register.inclusion_tag('django_lang_switch/dropdown.html')
def lang_switch_dropdown():
    """Render dropdown menu with available languages."""
    return {}
