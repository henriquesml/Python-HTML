class PyWeb(object):

    # Grava a TAG
    class Tag(object):
        global document
        document = []
        global n
        n = 4
        global page
        page = open('py.html', 'w')

        def __init__(self, doc, name, style, *text):

            self.name = name
            self.style = style
            self.text = text

            if text != ():
                page.write(text[0]+'\n')

        def __enter__(self):
            global n
            global page

            if self.name != 'html' and self.name  != '':
                page.write(' '*n+'<'+self.name+self.style+'>\n')
                n += 4

            else:
                 page.write('<'+self.name+'>\n')
            

        def __exit__(self, tpe, value, traceback):
            global n
            global page

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

    def text(self, strgs):
        global document
        global n

        return self.__class__.Tag(self, '', '',' '*n+strgs)

    def Content(self):
        return self, self.tag, self.text
