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
print(extrai_valor('A♦'))

def lista_movimentos_possiveis(baralho, indice):
    lista_jogadas = []
    if indice == 0:
        return lista_jogadas
    elif indice < len(baralho):      
        lista_naipe = []
        for i in range(len(baralho)):
            naipe = extrai_naipe(baralho[i])
            lista_naipe.append(naipe)