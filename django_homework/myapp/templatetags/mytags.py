from django import template
import random
from string import ascii_letters
register = template.Library()


@register.simple_tag
def random_number():
    return random.randrange(1, 100)


@register.simple_tag
def random_name():
    return ''.join(random.choice(ascii_letters) for i in range(random.randrange(5, 10)))
