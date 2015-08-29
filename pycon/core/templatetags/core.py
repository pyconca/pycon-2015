from django import template
from django.core.urlresolvers import reverse
from django.utils.translation import activate, get_language

register = template.Library()


@register.simple_tag(takes_context=True)
def lang_url(context, new_lang):
    """
    Returns current URL equivalent for new_lang
    For example, http://localhost/en/ might become http://localhost/fr/
    :param context: Template context provided by @register.simple_tag()
    :param new_lang: The language the URL should be for
    :return:
    """

    url_name = context.request.resolver_match.url_name
    cur_lang = get_language()
    activate(new_lang)
    new_url = reverse(url_name)
    activate(cur_lang)
    return new_url


@register.filter(name='get')
def get(value, arg):
    return getattr(value, arg)


@register.filter(name='i18n_get')
def i18n_get(value, arg):
    key = '{}_{}'.format(arg, get_language())
    return getattr(value, key, '')
