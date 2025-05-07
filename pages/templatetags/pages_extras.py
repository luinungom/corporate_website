from django import template
from pages.models import Pages

register = template.Library()

@register.simple_tag
def get_pages_list():
    pages = Pages.objects.all()
    return pages