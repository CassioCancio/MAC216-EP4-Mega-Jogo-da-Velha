from partida import Partida
from random import randint

class Aleatoria(Partida):
    def __init__(self, tipo_jogador_1: int, tipo_jogador_2: int):
        Partida.__init__(self, tipo_jogador_1, tipo_jogador_2)
   
    def proximo_jogador(self) -> int:
        ''' Sorteia entre o jogador 1 e 2 qual será o próximo'''
        return randint(0,1)