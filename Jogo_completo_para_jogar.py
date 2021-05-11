

print('|Paciência Acordeão|\n" + "====================.\n' )
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n')
print('Existem apenas dois movimentos possíveis:\n' )
print('1. Empilhar uma carta sobre a carta imediatamente anterior')
print('2. Empilhar uma carta sobre a terceira carta anterior.\n')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')
print('1. As duas cartas possuem o mesmo valor') 
print('ou')
print('2. As duas cartas possuem o mesmo naipe.\n')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')
enter = input('Aperte [ENTER] para para iniciar o jogo...')


if enter == "":
    x = cria_baralho()
    baralho_jogo = (sp(x, k=52))
    print(numero_colorido(baralho_jogo))
    baralho = numero_colorido(baralho_jogo)
    while lista_movimentos_possiveis:
        
        card = int(input('Escolha uma carta (digite um número entre 1 e {}):   '.format(len(baralho_jogo))))
                
        possiveis = lista_movimentos_possiveis(baralho_jogo, (card-1))
        if possiveis == [1, 3]:
            opcao1 = print('1. {}'.format(baralho_jogo[card-2]))
            opcao2 = print('3. {}'.format(baralho_jogo[card-4]))
            pergunta = int(input('Sobre qual carta você quer empilhar o {}: '.format(baralho_jogo[card-1])))
            baralho = empilha(baralho_jogo, card-1, (card-1)-pergunta)

        elif possiveis == [1]:
            print(empilha(baralho_jogo, card-1, card-2))

        elif possiveis == [3]:
            print(empilha(baralho_jogo, card-1, card-4))

        elif possiveis == []:
            print('A carta {} não pode ser movida. '.format(baralho_jogo[card-1]))

    if lista_movimentos_possiveis == False and len(baralho_jogo) == 0 :
        print('PARABÉNS!! Você é um gênio, ganhou o jogo!!')

    elif lista_movimentos_possiveis == False and len(baralho_jogo) != 0:
        print('Você perdeu :(')