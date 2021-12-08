from mega_tabuleiro import MegaTabuleiro
from sub_tabuleiro import SubTabuleiro

class Jogador:
    nome_jogador = ""
    simbolo = ""

    def __init__(self, nome_jogador, simbolo):
        self.nome_jogador = nome_jogador
        self.simbolo = simbolo
    
    def fazer_jogada(self):
        pass
