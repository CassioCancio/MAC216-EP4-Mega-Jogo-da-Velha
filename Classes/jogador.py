from mega_tabuleiro import MegaTabuleiro
from sub_tabuleiro import SubTabuleiro

class Jogador:
    nome_jogador: str
    simbolo: str

    def __init__(self, nome_jogador, simbolo):
        self.nome_jogador = nome_jogador
        self.simbolo = simbolo

    def receber_nome(self):
        return self.nome_jogador
   
    def receber_simbolo(self):
        return self.simbolo
