from django import template

register = template.Library()


@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + ' تومان'


@register.filter(name='discount')
def price_discount(value: int):
    return str(value) + '%'
