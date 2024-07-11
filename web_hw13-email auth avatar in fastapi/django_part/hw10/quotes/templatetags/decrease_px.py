from django import template

register = template.Library()

@register.simple_tag
def decreasing_font_size(start_size, step, iteration):
    return start_size - (step * iteration)