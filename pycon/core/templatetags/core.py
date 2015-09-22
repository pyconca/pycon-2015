from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
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
    
    cur_lang = get_language()
    activate(new_lang)
    resolver_match = context.request.resolver_match

    new_url = reverse(
        viewname = resolver_match.url_name,
        args = resolver_match.args,
        kwargs = resolver_match.kwargs
    )

    activate(cur_lang)
    
    return new_url


@register.filter(name='get')
def get(value, arg):
    return getattr(value, arg)


@register.filter(name='i18n_get')
def i18n_get(value, arg):
    key = '{}_{}'.format(arg, get_language())
    return getattr(value, key, '')
