from random import sample as sp
def cria_baralho():
    baralho = []
    espadas = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
    copas = ['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥']
    ouros = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦']
    paus = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    baralho = espadas + copas + ouros + paus
    return baralho

def extrai_naipe(carta):
    if '♦' in carta:
        return '♦'
    elif '♥' in carta:
        return '♥'
    elif '♣' in carta:
        return '♣'
    elif '♠' in carta:
        return '♠'  

def extrai_valor(carta):
    if '♦' in carta:
        removed = carta.replace('♦', "")
        return removed
    elif '♥' in carta:
        removed = carta.replace('♥', "")
        return removed 
    elif '♣' in carta:
        removed = carta.replace('♣', "")
        return removed 
    elif '♠' in carta:
        removed = carta.replace('♠', "")
        return removed 

def lista_movimentos_possiveis(baralho, indice):
    lista_jogadas = []
    if indice == 0:
        return lista_jogadas
    elif indice < len(baralho):      
        lista_naipe = []
        for i in range(len(baralho)):
            naipe = extrai_naipe(baralho[i])
            lista_naipe.append(naipe)
            lista_numero = []       
        for e in range(len(baralho)):    
            numero = extrai_valor(baralho[e])
            lista_numero.append(numero)
        if lista_naipe[indice] == lista_naipe[indice-1]:
            lista_jogadas.append(1)
        elif lista_numero[indice] == lista_numero[indice-1]:
            lista_jogadas.append(1)  
        if lista_naipe[indice] == lista_naipe[indice-3] and ((indice - 3) >= 0):
            lista_jogadas.append(3)
        elif lista_numero[indice] == lista_numero[indice-3] and ((indice - 3) >= 0):
            lista_jogadas.append(3)       
        return lista_jogadas

def empilha(baralho,origem,destino):
    if origem > destino:
        baralho[destino] = baralho[origem]
        del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    lista_nova = []
    for i in range(0, len(baralho)):
        if lista_movimentos_possiveis(baralho, i) == []:
            lista_nova.append(0)
        else:
            lista_nova.append(1) 
    for e in lista_nova:
        if e == 0:
            del(e)
    if lista_nova == []:
        return False
    else:
        return True 

x = cria_baralho()
baralho_jogo = (sp(x, k=52))

class pintar:
    reset='\033[0m'
    vermelho = '\033[1;31;40m'
    black = '\033[1;30m'

def colorir_carta(carta):
    if extrai_naipe(carta) == '♣' or extrai_naipe(carta) == '♠':
        carta = pintar.black + carta + pintar.reset
    elif extrai_naipe(carta) == '♥' or extrai_naipe(carta) == '♦':
        carta = pintar.vermelho + carta + pintar.reset
    return carta

def numero_colorido(baralho):
    print('         O estado atual do baralho é:')
    print("   ")
    for i in range(0, len(baralho)):
        print(str(i + 1) + ". " + colorir_carta(baralho[i]))
print(numero_colorido(baralho_jogo))


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
            print(numero_colorido(empilha(baralho_jogo, card-1, (card-1)-pergunta)))

        elif possiveis == [1]:
            print(numero_colorido(empilha(baralho_jogo, card-1, card-2)))

        elif possiveis == [3]:
            print(numero_colorido(empilha(baralho_jogo, card-1, card-4)))

        elif possiveis == []:
            print('A carta {} não pode ser movida. Por favor, escolha outra carta! '.format(baralho_jogo[card-1]))

    while lista_movimentos_possiveis == False:
        if len(baralho_jogo) == 1:
            print('PARABÉNS!! Você é um gênio, ganhou o jogo!!')
    
        elif len(baralho_jogo) > 1:
            print('Você perdeu :(.\n')
            jogar = input('Gostaria de jogar novamente? Responda com [sim ou não]. ')
            if jogar == 'sim':
                lista_movimentos_possiveis == True
            elif jogar == 'não':
                print('Obrigado por jogar!')