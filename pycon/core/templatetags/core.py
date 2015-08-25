from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import activate

register = template.Library()


@register.simple_tag(takes_context=True)
def lang_url(context, lang):
    url_name = context.request.resolver_match.url_name
    activate(lang)
    return reverse(url_name)
