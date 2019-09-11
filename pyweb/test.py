from pyweb import *

doc, tag, text = PyWeb().Content()

with tag('html'):
    with tag('h1'):
        text('Olá Mundo')
    with tag('h2'):
        text('Olá Mundo')

PyWeb().Generate()
