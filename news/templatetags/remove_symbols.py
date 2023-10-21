import re
from . import register
from django.template.defaultfilters import stringfilter


@register.filter
@stringfilter
def clear_end_text(s: str):
    s = re.sub(r'^(.*\w)[^\w]*$', r'\1', s, flags=re.DOTALL)
    return s

