from django import template

register = template.Library()

@register.simple_tag
def path_split(request_data: str):
    return request_data.split('/')[2]