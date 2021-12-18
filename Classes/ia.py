from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class IA(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)
