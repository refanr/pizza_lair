from django import template

register = template.Library()

@register.filter
def get_pizza_count(pizza_counts, pizza_name):
    return pizza_counts.get(pizza_name, 0)

register.filter('get_pizza_count', get_pizza_count)
