class PyWeb(object):

    # Grava a TAG
    class Tag(object):

        global n
        n = 4
        global page
        page = open('py.html', 'w')

        def __init__(self, doc, name, style, *text):

            self.name = name
            self.style = style
            self.text = text

            # Se for informado texto
            if text != ():
                page.write(text[0]+'\n')

        def __enter__(self):
            global n
            global page

            # Grava a abertura da tag
            if self.name != 'html' and self.name  != '':
                page.write(' '*n+'<'+self.name+self.style+'>\n')
                n += 4
            else:
                 page.write('<'+self.name+'>\n')
            
        def __exit__(self, tpe, value, traceback):
            global n
            global page

            # Grava o fechamento da tag
            if self.name != 'html':
                n -= 4
                page.write(' '*n+'</'+self.name+'>\n')
            else:
                page.write('<'+self.name+'>\n')

    def tag(self, tag_name, *style):
        if style != ():
            newstyle = ' '+style[0]
        else:
            newstyle = ''

        return self.__class__.Tag(self, tag_name, newstyle)

    def button(self, *strgs):
 
        return self.__class__.Tag(self, 'button','')

    def text(self, strgs):
        global n

        return self.__class__.Tag(self, '', '',' '*n+strgs)

    def Content(self):
        return self, self.tag, self.text , self.button
