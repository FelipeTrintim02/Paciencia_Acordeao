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
print(extrai_naipe('A♦'))