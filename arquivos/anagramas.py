"""

 Autor: RaolootneXII :)

 Objetivo: Calcular por meio de uma permutação,
 simples ou com repetição, o número de combinações
 de um termo, mostra o número de combinações e, se
 caso o usuário queira, printar cada uma das combi
 nações e coloca-lás em um documento de texto.
    
 Atualizado em 05-10-2017.

"""
# Importações
# Uso o metodo dessa biblioteca para ver quantas
# vezes uma letra ou um número repete em uma String.
from collections import Counter
# Uso o metodo dessa biblioteca para gera um
# número aleatório.
from random import randint


# Funções

# Essa função calcula o fatorial. Para isso ela
# recebe um número que será fatorado, cria uma
# variável para armazenar o resultado, e manda
# um estruta de repetição que vai rodar enquanto
# num for maior que 1(poderia ser maior ou igual
# já que multiplicando por 1 não muda), ele mul-
# tiplica o valor do num pelo resul e adicona
# ao resul, diminuir 1 da variável num e retor-
# na de novo até que seja igual a 1. Após isso
# ele retorna o valor do resultado pela variavel
# result.

def fatorial(num):
    resul = 1  # Cria a variável resul.
    while num > 1:  # Incia o loop.
        resul *= num  # Vai multiplicando para formar o fatorial.
        num -= 1  # Retira 1 da variavel num.
    return resul  # Retorna o resultado.



# Essa função simplesmente retorna as letra que a palavra tem
# num vetor. Para isso ele simplesmente usa um while que vai
# rodar enquanto um contador for diferente da quantidade
# de letras, dentro desse while ele adiciona a letra atual,
# que é o número do contador, num lista. E esse while roda
# até que contador seja igual a quantidade de letras. Chegou
# na quantidade de letras, ele retorna essa lista.

def retorna():
    lista = list()  # Cria uma lista.
    contador = 0  # Cria um contador.
    while contador != len(palavra):  # Roda o while cuja
        lista.append(palavra[contador])  # funcionalidade
        contador += 1  # Já foi descrita acima.
    return lista  # retorna a lista.


menu = True  # Variavel de Menu basica
while menu:
    print('Permutação Simples e Com repetição')  # Coisas apenas usadas
    print('----------------------------------')  # pra ficar bonito.
    palavra = input('Escreva a palavra ou os números: ')  # Pergunto a palavra ou números ou os dois.

    # Quantidade de Combinações

    # Variáveis
    palavraR = Counter(palavra)  # Variável que vai receber uma lista dos termos que se
    # repetem e quantas vezes eles repetem.
    quantidadeDeL = len(palavra)  # Variável que armazena a quantidade de letras.
    repeticoes = 1  # Variavel que armazena essas repetições de termos.
    # Contador usado para controlar um while.
    repeticoesF = 0

    # O for a seguir é utilizado para mostrar quantas vezes uma letra se repete
    # usando a variavel palavraR que é uma lista. Basicamente pra cada espaço
    # dessa lista ela vai ter uma posição no for, essa posição vai ser nesse caso
    # o i. Basicamente pra cada i dentro da lista palavraR, ele vai ver se o
    # valor na posição i é maior que 1, se sim, ele printa a letra que é o
    # i, printa também as vezes que aquela letra se repete que é a palavra
    # na posição i ou seja palavra[i] e por ultimo diz que repetições vai
    # receber o valor dela que é 0, a principio, e soma com número de
    # repetições que é a palavraR[i]

    for i in palavraR:
        if palavraR[i] > 1:  # Verifica se é maior que 1
            print('A letra {} se repete {} vezes'.format(i, palavraR[i]))  # printa
            repeticoes *= fatorial(palavraR[i])  # Adiciona a variavel repetição as vezes
            # que uma letra se repete

    # Esse if a seguir simplesmente ver se o número de reptições é igual a 0.
    # Basicamente só vai ser 0 quando no for anterior nenhuma letra se repetiu.
    # Se for igual a zero ele diz que repeticoes = 1 para que posteriormente
    # não ocorra nenhum erro de divisão por 0.
    if repeticoes == 0:  # Verifica
        repeticoes = 1  # Adiciona o valor 1 à variável repetição

    palavraF = fatorial(quantidadeDeL)  # Variavel que armazena o fatorial de todos os termos.

    # Calcula e printa o valor de combinações que é igual ao fatorial das
    # palavras dividida pelas repetições
    tCombinacoes = int(palavraF / repeticoes)
    print('Número total de combinações: {}'.format(tCombinacoes))

    # Anagramas

    menu2 = True  # Outra variavel usada para manter um menu
    while menu2:
        # Aqui ele faz uma pergunta se quer ou não mostrar os anagramas
        # Ele adiciona a entrada a variável escolha e executa algumas
        # Estruturas condicionais. Basicamente se a resposta da pergunta
        # for s ou S, ele mostra os Anagramas, se n ou N, ele pergunta
        # Se quer continuar permutando mais coisas ou não, se você dizer
        # que quer continuar permutando, ele define o menu2 como False
        # ou seja sai do menu do Anagrama, pula dois espaços e quebra o
        # while em que ele está, se você dizer que não quer continuar
        # ele simplesmente define ambos os menus 1 e 2 como False logo
        # sai de todos os menus e fecha o programa, no menu Anagrama
        # e no menu interno a eles se você escrever uma opção que não
        # consta ele pede para escrever algo valido.
        escolha = input('Deseja mostrar os possiveis anagramas?(s/n): ')
        if escolha == 's' or escolha == 'S':
            # Pensei em perguntar ao usuario se ele queria criar um docu-
            # mento com todos os arquivos ou não, mas achei legal fazer 
            # de cara. Os 3 comando abaixo servem respectivamente para:
            # criar um documento com a palavra, escrever um cabeçalho com 
            # a palavra e o número de combinações e por ultimo fecha o 
            # arquivo.
            arq = open('{}.txt'.format(palavra), 'w')
            arq.writelines(
            'Anagramas com a palavra "{}"\nTotal: {}\n\n'.format(palavra, tCombinacoes))
            arq.close()

            # Variáveis
            anagramas = 0  # Variável que irá armazenar quantos anagramas
            # Já foram feitos.
            ana = ''  # Essa variável define o anagrama em um periodo de
            # tempo.
            listaletras = retorna()  # Criando uma lista com cada termo.
            # da palavra.
            geral = list()  # Criando uma lista para guardar todos os
            # anagramas montados, para depois que houver uma nova mon-
            # tagem de um anagrama, poder conferi se ele já existe ou
            # não, logo, essa lista serve para que Anagramas não se re-
            # pitam.
            contadorBug = 0  # Por algum motivo, em alguns momentos o
            # programa simplesmente para num dos while, logo essa va-
            # riável é fundamental pra quando ele entrar nesse while
            # e bugar ela começar a iniciar um contador e quando esse
            # contador chegar a um determinado número, sair do while
            # bugado e reseta por conta do bug.
            resetBug = False  # Essa variável é ativada quando o
            # bug for "diagnosticado" e ela simplesmente reseta o
            # loop à partir de uma estrutura condicional, if.

            # Esse while é meio complicado de explicar. Bom, ele vai
            # manter o loop enquanto o número de anagramas for di-
            # ferente do número de combinações possiveis. Dentro
            # dele as coisas complicam, primeiramente ele adiciona a
            # uma variavel numA um valor aleatório entre 0 e a quan-
            # tidade de letras menos 1(pra poder entrar no vetor já
            # que sua primeira posição é de 0), então ele vai dire-
            # to a um while que vai rodar enquanto o vetor das letras
            # na posição daquele número aleatorio(numA) for igual a
            # 'JáFoi', se caso não for igual a 'JáFoi' ele continua,
            # agora se for igual, ele entra no loop. Esse loop, ba-
            # sicamente, fica sorteando o número até que não seja
            # um número que já foi, e é nesse loop que entra o
            # bug por isso tem um contador, esse contador vai meio
            # que definir um número de tentativas máximas, que é
            # uma "definição" desse bug, sendo igual ou maior que
            # esse número de tentativas máximas, ele entra numa
            # estrura if que seta contadorBug como 0, ativa o
            # reset bug e quebra o while que está bugado, assim
            # logo quando sai ele vai direto no if que verifica
            # se reset bug foi ativado ou não, se foi, ele re-
            # torna o valor da lista com todas as letras, zera
            # o anagrama(ana) , define reset bug como False e
            # da um continue para o while começar de novo. Su-
            # pondo que não tenha entrado nessa condição ele
            # simplesmente pega o valor de ana e adiciona
            # aquele listaletras na posição numA ou seja
            # ele só vai chegar aí se essa posição nunca
            # tiver caido e se não tiver bugado nada, depois
            # disso ele seta o listaletras na posição numA
            # que já foi usada como 'JáFoi' para que posterior-
            # mente não venha uma mesma letra a se repetir.
            # Por ultimo ele verifica se o valor dos termos
            # de ana(anagrama) é igual a o valor dos termos
            # da palavra que foi dada no inicio do programa
            # e se o valor de ana não ja existe na lista geral,
            # se não retornar False, ele sai, se retornar True,
            # ele adiciona na lista geral o valor que ana
            # possui, printa o anagrama que está(ta: anagrama
            # + 1, pois anagrama se incia do 0 ou seja se o
            # valor total do anagramas for 6, ele vai de 0 a 5,
            # logo, esse +1 corrige isso) e o anagrama em si,
            # define o ana(anagrama) como vazio, soma 1
            # ao anagrama para que em um momento ele seja
            # igual as combinações e saia do loop, retornar
            # o valor do listaletras, ou seja, adiciona uma
            # lista com as letras da palavra e por ultimo
            # diz que a variavel contadorBug é igual a 0.
            while anagramas != tCombinacoes:  # Inicia o loop.
                numA = randint(0, (len(palavra) - 1))  # Ver um número aleatório.
                while listaletras[numA] == 'JáFoi':  # confere se o valor naquela
                    # posição de número aleatório ja foi.
                    numA = randint(0, (len(palavra) - 1))  # Ver um número aleatório.
                    contadorBug += 1  # Soma 1 no contadorBug.
                    if contadorBug >= 20:  # Ver se o contadorBug é >= a 20.
                        contadorBug = 0  # Seta contadorBug como 0.
                        resetBug = True  # Ativa a variavel resetBug.
                        break  # Quebra o loop.
                if resetBug:  # Se resetBug == True.
                    listaletras = retorna()  # Adiciona a lista com os termos.
                    ana = ''  # Zera ana(anagramas).
                    resetBug = False  # Define resetBug como False.
                    continue  # Executa o while de novo sem continuar o resto.
                ana += listaletras[numA]  # Adiciona a ana o valor em letra.
                listaletras[numA] = 'JáFoi'  # Define como ja foi o a letra adicionada.
                if len(ana) == len(palavra) and ana not in geral:  # Faz essa condição

                    # -------------------------------------------------------------
                    # Essa parte do código foi adicionada depois de minha pessoa
                    # ter terminado de comentar o código inteiro, então, achei
                    # melhor explicar o que faz aqui do que mexer naquele textão
                    # lá em cima. Bom cada codigo faz, respectivamente, abre o 
                    # documento(para leitura), adiciona o que está dentro desse
                    # documento numa variavel, fecha o arquivo, como cada linha
                    # de um documento é uma posição de uma lista usei o append
                    # para adicionar uma nova linha com o número do anagrama
                    # e o anagrama, abre o arquivo(para escrita), escreve o 
                    # conteúdo que estava na variável temporária e fecha o 
                    # arquivo.
                    arq = open('{}.txt'.format(palavra), 'r')
                    conteudoTemp = arq.readlines()
                    arq.close()
                    conteudoTemp.append('{} - {}\n\n'.format((anagramas + 1), ana))
                    arq = open('{}.txt'.format(palavra), 'w')
                    arq.writelines(conteudoTemp)
                    arq.close()
                    # -------------------------------------------------------------

                    geral.append(ana)  # Adiciona a lista geral o valor de ana.
                    print('{}# - {}'.format((anagramas + 1), ana))  # Printa os valores.
                    ana = ''  # Define ana(anagramas) como 0.
                    anagramas += 1  # Soma um no valor de anagramas.
                    listaletras = retorna()  # Adiciona a lista com os termos.
                    contadorBug = 0  # Diz que a variavel contadorBug é igual a 0.

            # Esse while pergunta ser o ser deseja continuar tem a mesma utilidade do
            # while que foi explicado lá em cima, inclusive, é o mesmo.
            while menu:
                escolha = input('Deseja continuar calculando Permutações?(s/n): ')  # Pergunta.
                if escolha == 's' or escolha == 'S':  # Ver se é s ou S.
                    menu2 = False  # Se sim ele sai do menu2( menu dos anagramas ),
                    print('\n\n')  # inicia o programa de novo,
                    break  # e quebra o loop.
                elif escolha == 'n' or escolha == 'N':  # Ver se é n ou N.
                    menu = False  # se sim ele sai de todos os menus.
                    menu2 = False
                else:  # Se algo digitado não for igual a nada que foi pedido ele pede que escreva
                    # uma opção valida.
                    print('\n\n')
                    print('Digite uma opção válida')
        elif escolha == 'n' or escolha == 'N':
            while menu:
                escolha = input('Deseja continuar calculando Permutações?(s/n): ')  # Pergunta.
                if escolha == 's' or escolha == 'S':  # Ver se é s ou S.
                    menu2 = False  # Se sim ele sai do menu2( menu dos anagramas ),
                    print('\n\n')  # inicia o programa de novo,
                    break  # e quebra o loop.
                elif escolha == 'n' or escolha == 'N':  # Ver se é n ou N.
                    menu = False  # se sim ele sai de todos os menus.
                    menu2 = False
                else:  # Se algo digitado não for igual a nada que foi pedido ele pede que escreva
                    # uma opção valida.
                    print('\n\n')
                    print('Digite uma opção válida')
        else:  # Se algo digitado não for igual a nada que foi pedido ele pede que
            # uma opção valida.
            print('\n\n')
            print('Digite uma opção válida')
