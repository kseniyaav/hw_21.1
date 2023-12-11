from django import template

register = template.Library()


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'

    return '#'


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'

    return '#'
