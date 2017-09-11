function iniciar(){
	var imgs = new Array('imagens/n1.jpg','imagens/n2.jpg','imagens/n3.jpg');
  	for (var i = 0; i < imgs.length; i++) {
  		var image = new Image();
  		image.src = imgs[i];
  	}
  	fi = 1;
  	window.setInterval('proxN()', 15000);
}

function trocarNoticia(){
	if (fi == 1) {
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - Mudanças!! (Bra)';
		document.getElementById('noticiaP').innerHTML = 'Para aumentar o conteúdo do site, '+
		'mudanças precisam acontecer, foi pensando nisso que agora nosso site é administrado '+ 
		'por 3 pessoas: Topem, lElaPhodusy e Brashilo, cada um terá um post sobre a sua '+
		'personalidade, que pode ser acessado pelo menu logo a cima, explicando algumas coisas '+ 
		'e servindo de introdução para, basicamente...';
		document.getElementById('noticiaL').href = 'posts/2017/setembro/mudancas.html';
		document.getElementById('noticiaN').innerHTML = '1/3';
		document.getElementById('noticiaF').src = 'imagens/n1.jpg';
	}
	else if (fi == 2){
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - Mudou (Bra)';
		document.getElementById('noticiaP').innerHTML = '"Ultimamente nada, nada me '+
		'interessa. Nem uma conversa. Eu não sinto pressa, saudade ou paixão...". '+
		'Talvez essa seja a música que mais faz sentido na minha vida no momento '+
		'atual. Antigamente parecia legal a ideia de estar junto de outras pessoas '+ 
		'compartilhando histórias, hoje não vejo prazer algum nisso...';
		document.getElementById('noticiaL').href = 'posts/2017/setembro/mudou.html';
		document.getElementById('noticiaN').innerHTML = '2/3';
		document.getElementById('noticiaF').src = 'imagens/n2.jpg';
	}
	else if (fi == 3){
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - Folclore (Bra)';
		document.getElementById('noticiaP').innerHTML = 'O dia começou as 5 horas da manhã, '+
		'o sono me consumia, lembro de ter sonhado, mas, não lembro com o que. O objetivo era '+ 
		'que todos da minha equipe estivessem na escola de 6 horas, sendo que a escola abre as '+ 
		'7 horas, para que nós pudéssemos ensaiar. O problema foi que só chegou eu e mais uma '+
		'amiga, os outros 3 não vieram, além disso...';
		document.getElementById('noticiaL').href = 'posts/2017/agosto/diafolclore.html';
		document.getElementById('noticiaN').innerHTML = '3/3';
		document.getElementById('noticiaF').src = 'imagens/n3.jpg';
	}
	
}

function proxN(){
	fi++;
	if (fi > 3) {
		fi = 1;
	}
	trocarNoticia();
}
function anterN(){
	fi--;
	if (fi < 1) {
		fi = 3;
	}
	trocarNoticia();
}