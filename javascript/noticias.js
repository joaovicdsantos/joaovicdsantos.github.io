function iniciar(){
	var imgs = new Array('imagens/n1.jpg','imagens/n2.jpg','imagens/n3.jpg');
  	for (var i = 0; i < imgs.length; i++) {
  		var image = new Image();
  		image.src = imgs[i];
  	}
  	fi = 1;
  	tmr = setInterval('trocaN(1)', 15000);
}

function trocarNoticia(){
	if (fi == 1) {
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - Anagramas (Bra)';
		document.getElementById('noticiaP').innerHTML = 'A ideia surgiu aleatoriamente, ' +
		'enquanto o professor de matemática resolvia alguns exercicios de Análise '+
		'Combinatória. A permutação com a palavra "periquito" deu exatamente 181.440, ele, '+
		'ironicamente, disse que quem quisesse fazer o anagrama inteiro em casa podia, nesse '+
		'momento eu até perguntei alto "E se eu fizesse?"...';
		document.getElementById('noticiaL').href = 'posts/2017/outubro/anagramas.html';
		document.getElementById('noticiaN').innerHTML = '1/3';
		document.getElementById('noticiaF').src = 'imagens/n1.jpg';
	}
	else if (fi == 2){
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - 17:37 (Topem)';
		document.getElementById('noticiaP').innerHTML = 'Tudo comecou normal, em 2016, um '+
		'pouco mais que a metade do ano, para ser mais exata, nada fora do lugar, acordei, '+
		'escovei os dentes, tomei café, banho, almocei e várias coisas no meio tempo dos '+
		'mesmos, e exatamente 12:30 lá estava eu pegando a bicicleta e indo para o colégio...';
		document.getElementById('noticiaL').href = 'posts/2017/setembro/17:37.html';
		document.getElementById('noticiaN').innerHTML = '2/3';
		document.getElementById('noticiaF').src = 'imagens/n2.jpg';
	}
	else if (fi == 3){
		document.getElementById('noticiaT').innerHTML = 'Ultimos Posts - Dia do Led (Bra)';
		document.getElementById('noticiaP').innerHTML = 'Esse dia é mais um exemplo de que a '+
		'felicidade está nas pequenas coisas do dia e se a gente não perceber isso acaba '+
		'tentando buscar a felicidade em outras coisas. Bom nós, eu e 4 pessoas da minha '+
		'equipe, tínhamos um trabalho de química, o objetivo era acender um simples Led com '+
		'batata e limão, mas, nós não tínhamos o Led então tivemos que comprar....';
		document.getElementById('noticiaL').href = 'posts/2017/setembro/led.html';
		document.getElementById('noticiaN').innerHTML = '3/3';
		document.getElementById('noticiaF').src = 'imagens/n3.jpg';
	}
	
}

function trocaN(proxORant){
	clearInterval(tmr);
	fi += proxORant;
	if (fi > 3) {
		fi = 1;
	}
	else if (fi < 1){
		fi = 3;
	}
	trocarNoticia();
	tmr = setInterval('trocaN(1)', 15000);
}