from pyweb import *

doc, tag, text = PyWeb().tagtext()

with tag('html'):
    with tag('h1'):
        text('Olá Mundo')

