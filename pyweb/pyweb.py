class PyWeb(object):

    # Grava a TAG
    class Tag(object):
        global document
        document = []
        global n
        n = 4

        def __init__(self, doc, name, *text):

            self.name = name
            self.text = text

        def __enter__(self):
            global n
            if self.name != 'html' and self.name  != '':
                document.append(' '*n+'<'+self.name+'>')
                n += 4
                if self.text != '':
                    document.append(self.text)
            else:
                document.append('<'+self.name+'>')

        def __exit__(self, tpe, value, traceback):
            global n
            if self.name != 'html':
                n -= 4
                document.append(' '*n+'</'+self.name+'>')
            else:
                document.append('<'+self.name+'>')

    def tag(self, tag_name, *args, **kwargs):

        return self.__class__.Tag(self, tag_name)

    def text(self, strgs):

        return self.__class__.Tag(self,'',strgs)

    def Content(self):
        return self, self.tag, self.text

    def Generate(self):
        global document
        print(document)

        for i in document:
            print(i)


