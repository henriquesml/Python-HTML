from pyweb import *

tag, text, button = PyWeb().Content()

texto = ('''
    style="color: red;
    font-family: Arial"''')

with tag('html'):
    with tag('h1', texto):
        text('Olá Mundo')
    with tag('h2', texto):
        text('Olá Mundo')
    with button():
        text('botão')
