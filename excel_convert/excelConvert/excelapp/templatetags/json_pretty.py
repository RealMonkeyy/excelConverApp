import json
from django import template

register = template.Library()

@register.filter(name='json_pretty')
def json_pretty(value):
    try:
        return json.dumps(json.loads(value), indent=4, ensure_ascii=False)
    except (ValueError, TypeError):
        return value