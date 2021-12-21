from partida import Partida

class Comum(Partida):
    proximo: int
    
    def __init__(self, jogador1, jogador2):
        Partida.__init__(self, jogador1, jogador2)
        self.proximo = 0

    def proximo_jogador(self):
        atual = self.proximo
        self.proximo = 1 if self.proximo == 0 else 0
        return atual