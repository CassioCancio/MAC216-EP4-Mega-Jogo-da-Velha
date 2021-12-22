from partida import Partida

class Comum(Partida):
    proximo: int


    def __init__(self, tipo_jogador_1: int, tipo_jogador_2: int):
        Partida.__init__(self, tipo_jogador_1, tipo_jogador_2)
        self.proximo = 0


    def proximo_jogador(self) -> int:
        ''' Envia o id que representa qual o próximo jogador, respeitando uma rodada para cada jogador '''
        # Pega o id atual
        atual = self.proximo

        # Troca para o outro valor
        self.proximo = 1 if self.proximo == 0 else 0

        return atual