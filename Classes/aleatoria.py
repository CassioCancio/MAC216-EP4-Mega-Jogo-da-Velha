from partida import Partida
from random import randint
class Aleatoria(Partida):
    def __init__(self, jogador1, jogador2):
        Partida.__init__(self, jogador1, jogador2)

    def fazer_jogada(self):
        atual = randint(0,1)
        print(f"Pelo sorteio, é a vez de {self.receber_nome_jogador(atual)} ({self.receber_simbolo_jogador(atual)})")
        self.jogadores[atual].preparar_jogada(self.tabuleiro)
        id_jogador = self.tabuleiro.receber_vencedor()
        if id_jogador != None: self.finalizar()