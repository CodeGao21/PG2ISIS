# custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_stage(dictionary, key):
    return dictionary.get(key, 0)
