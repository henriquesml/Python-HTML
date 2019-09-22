from pyweb import *

doc, tag, text = PyWeb().Content()

texto = ('style="color: blue"')

with tag('html'):
    with tag('h1', texto):
        text('Olá Mundo')
    with tag('h2'):
        text('Olá Mundo')

