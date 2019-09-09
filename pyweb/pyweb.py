class PyWeb(object):
    
    # Grava a TAG
    class Tag(object):

        global document
        document = []

        def __init__(self, doc, name):

            self.name = name

        def __enter__(self):
            global document
            document.append(self.name)
            print(document)

            global x
            x = len(document)

        def __exit__(self, tpe, value, traceback):

            global x

            document.append(document[x-1])
            print(document)

            x -= 1
        

	#aqui entra a tag
    def tag(self, tag_name, *args, **kwargs):

        return self.__class__.Tag(self, tag_name)


    def text(self, *strgs):
        print(strgs)

    def Content(self):
        return self, self.tag, self.text

    def Generate(self):
        global document
        for i in document:
            print(i)

