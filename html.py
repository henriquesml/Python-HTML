# string com o código HTML
codigo_html = '''
<html>
<head>
<title>Html com Python</title>
<script src="script.js"></script>
</head>

<body>
<center>
	<h1><a href="">Gerando arquivos HTML com python</a></h1>
	<h3>Python é a melhor linguagem do mundo!</h3>
	<div id="div1">
		<textarea id="textarea1" rows="4" cols="50">Digite algo aqui...</textarea><br/><br/>
		<button onclick="mostrar_conteudo()">Executar</button>
	</div>
</center>
</body>
</html>
'''

# string com o código JavaScript
codigo_javascript = '''
function mostrar_conteudo() {
	var elem = document.getElementById("textarea1");
	var texto = elem.value;

	alert("O texto digitado possui " + texto.length + " caracteres.");
}
'''

# abre o arquivo HTML para escrita
arq_html = open('index.html', 'w')

# abre o arquivo JavaScript para escrita
arq_js = open('script.js', 'w')

# escrevendo no arquivo HTML
arq_html.write(codigo_html)

# escrevendo no arquivo JavaScript
arq_js.write(codigo_javascript)

# fechando os arquivos
arq_html.close()
arq_js.close()
