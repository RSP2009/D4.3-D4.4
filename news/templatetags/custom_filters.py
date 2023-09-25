from django import template
import re

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает
# где именно их искать и фильтры потеряются :(


@register.filter(name='Censor')
def censor(value):
    with open('words.txt', 'r', encoding='utf-8') as f:
        bad_words = f.read().split()
        for w in bad_words:
            word = r'\b{}\b'.format(w)
            value = re.sub(word, '!п-'+'и-'*len(w)+'п!', value)
        return value
