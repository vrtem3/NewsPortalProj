from django import template
 
register = template.Library()


@register.filter(name='censor')
def censor(text):

    replace_values = {'lol': 'l**', 'bot': 'b**'}

    for i, j in replace_values.items():
        text = text.replace(i, j)
    return text

