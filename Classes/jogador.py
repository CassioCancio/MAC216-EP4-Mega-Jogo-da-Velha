from mega_tabuleiro import MegaTabuleiro
from sub_tabuleiro import SubTabuleiro
import time

class Jogador:
    nome_jogador: str
    simbolo: str


    def __init__(self, nome_jogador: str, simbolo: str):
        self.nome_jogador = nome_jogador
        self.simbolo = simbolo

    
    def esperar(self) -> None:
        time.sleep(2)


    def receber_nome(self) -> str:
        return self.nome_jogador

   
    def receber_simbolo(self) -> str:
        return self.simbolo
