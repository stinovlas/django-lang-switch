"""Language switch template tags."""
from django import template

register = template.Library()


@register.inclusion_tag('django_lang_switch/dropdown.html')
def lang_switch_dropdown(redirect_to: str = None):
    """
    Render dropdown menu with available languages.

    Args:
        redirect_to: Where to redirect after language change.

    Returns:
        Rendered select box language switch.

    """
    return {'redirect_to': redirect_to}
