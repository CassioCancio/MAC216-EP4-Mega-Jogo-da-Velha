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
        ''' Faz com que os jogadores não humanos esperem para que o usuário possa ver as jogadas'''
        time.sleep(2)


    def receber_nome(self) -> str:
        ''' Devolve o nome do jogador '''
        return self.nome_jogador

   
    def receber_simbolo(self) -> str:
        ''' Devolve o símbolo do jogador '''
        return self.simbolo
