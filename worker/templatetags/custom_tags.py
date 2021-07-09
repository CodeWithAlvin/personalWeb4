from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    try:
        return value.split(key)
    except:
        return None