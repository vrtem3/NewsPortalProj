from django import template
 
register = template.Library()


@register.filter(name='censor')
def censor(text):

    replace_values = {'lol': 'l**', 'bot': 'b**'}

    for i, j in replace_values.items():
        text = text.replace(i, j)
    return text


# Эталонное решение фильтра цензуры
# STRONG_WORDS = ["php", "редиска"]


# @register.filter()
# def censor(value):
#   if not isinstance(value, str):
#       raise ValueError('Нельзя цензурировать не строку')
#
#   for word in STRONG_WORDS:
#       value = value.replace(word[1:], '*' * (len(word)-1))
#
#   return value