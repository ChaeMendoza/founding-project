from django import template
register = template.Library()

@register.simple_tag
def porcentaje(a: float, b: float):
    return round((a / b) * 100, 2)