from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def format_timestamp(value):
    delta = timezone.now() - value

    if delta.days < 1:
        minutes = delta.seconds // 60
        if minutes >= 60:
            hours = minutes // 60
            return f'{hours}h'
        else:
            return f'{minutes}m'
    else:
        return value.strftime('%m/%d/%Y')
