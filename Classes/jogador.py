from mega_tabuleiro import MegaTabuleiro
from sub_tabuleiro import SubTabuleiro
import time

class Jogador:
    nome_jogador: str
    simbolo: str


    def __init__(self, nome_jogador, simbolo):
        self.nome_jogador = nome_jogador
        self.simbolo = simbolo

    
    def esperar(self):
        time.sleep(2)


    def receber_nome(self):
        return self.nome_jogador

   
    def receber_simbolo(self):
        return self.simbolo
