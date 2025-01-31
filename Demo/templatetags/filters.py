from django import template

register = template.Library()

@register.filter()
def count_total(value):
    count_total = 0
    for _ in value:
        count_total += 1
    return count_total