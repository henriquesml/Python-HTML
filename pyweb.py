class pyweb:

    # Variaveis globais
    def init(self, name):
        global _name
        _name = name

        global _body
        _body = ''
                
        global _div
        _div = ''

        global _div_content
        _div_content = ''

    # Metodo para adicionar o titulo na pagina
    def title_head(self, title):
        global _title
        _title = title

    #--------------DIV-----------------
    def div_body(self, div):

        global _body

        def 
    
        _body += '\n<div>\n'+div+'\n</div>\n'
        
    #--------------DIV-----------------
    

    #-----------PARAGRAFO--------------
    # Genérico
    def p_body(self, p):
        global _body  
        _body += '\n<p>'+p+'</p>\n'
        
    #----------------------------------

    #---------------H------------------
    def h_body(self, h):
        global _body  
        _body += '\n<h>'+h+'</h>\n'
    #----------------------------------

    #---------------A------------------
    def a_body(self, a):
        global _body  
        _body += '\n<a>'+a+'</a>\n'
    #----------------------------------

    #---------GRAVA EM HTML------------
    def generate(self):
        global _title
        global _name
        global _div
        global _body  
  
        try:
            _title = _title
        except NameError:
            _title = 'Page Name'

        html_code = '<html>\n'+'\n<head>\n'+'\n<title>'+_title+'</title>\n'+'\n</head>\n'+'\n<body>\n'+_body+'\n</body>\n'+'\n</html>'
        
        page = open(_name+'.html', 'w')
        page.write(html_code)
        page.close()
    #----------------------------------