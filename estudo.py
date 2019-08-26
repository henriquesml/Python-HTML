class html:
    def __init__(self, tags):
        self.tags = tags

    def getnome(self):

        return self.tags


nome = html('eae')

print(nome.getnome())
