from partida import Partida
from random import randint
class Aleatoria(Partida):
    def __init__(self, jogador1, jogador2):
        Partida.__init__(self, jogador1, jogador2)
    
    def proximo_jogador(self):
        return randint(0,1)