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
print(lista_movimentos_possiveis(['A♦', '10♥', 'Q♣', 'K♠', '10♣', '4♠'], 4))