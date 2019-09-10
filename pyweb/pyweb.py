class PyWeb(object):

    # Grava a TAG
    class Tag(object):

        global document
        document = []

        def __init__(self, doc, name):

            self.name = name

        def __enter__(self):
            document.append('<'+self.name+'>')

        def __exit__(self, tpe, value, traceback):
            document.append('</'+self.name+'>')
	#aqui entra a tag
    def tag(self, tag_name, *args, **kwargs):

        return self.__class__.Tag(self, tag_name)


    def text(self, *strgs):
        print(strgs)

    def Content(self):
        return self, self.tag, self.text

    def Generate(self):
        global document
        print(document)
        for i in document:
            print(i)

