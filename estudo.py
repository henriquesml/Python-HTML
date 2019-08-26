class html:
    title = ''
    p = ' '
    
    
    def title_html(self, x):
        global title
        title = '<title>'+x+'</title>'

    def p_html(self, x):
        global p
        p = x
        if p != ' ':
            p = '<P>\n'+'\n'+x+'\n'+'\n</P>'

    def set_(self):
        global title
        global p
        codigo_html = '<html>\n'+'\n<head>\n'+'\n'+title+'\n'+'\n</head>\n'+'\n<body>\n'+'\n</body>\n'+'\n</html>'
   
        codigo_html = '<html>\n'+'\n<head>\n'+'\n'+title+'\n'+'\n</head>\n'+'\n<body>\n'+'\n'+p+'\n'+'\n</body>\n'+'\n</html>'

        arq_html = open('pag.html', 'w')
        arq_html.write(codigo_html)
        arq_html.close()





nome = html()

nome.title_html('PAG')

nome.set_()
