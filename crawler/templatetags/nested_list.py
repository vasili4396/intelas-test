from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def form_data(data):
    text = "<ul>"
    for url, nested_urls in data.items():
        text += f'<li>{url}</li>'
        if isinstance(nested_urls, dict) and bool(nested_urls):
            text += f'<li style="list-style-type: none">{form_data(nested_urls)}</li>'

    text += "</ul>"
    return text


@register.simple_tag
def render_dict(data):
    text = form_data(data)
    return mark_safe(text)
