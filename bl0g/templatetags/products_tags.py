from django import template

from bl0g.models import Categories

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('bl0g/list_categories.html')
def show_categories():
    categories = Categories.objects.all()
    return {'categories': categories}