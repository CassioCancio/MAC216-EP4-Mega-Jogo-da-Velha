from partida import Partida

class Comum(Partida):
    proximo_a_jogar: int

    def __init__(self, jogador1, jogador2):
        Partida.__init__(self, jogador1, jogador2)
        self.proximo_a_jogar = 0

    def fazer_jogada(self):
        atual = self.proximo_a_jogar
        self.proximo_a_jogar = 1 if atual == 0 else 0
        print(f"É a vez de {self.receber_nome_jogador(atual)}")
        linha,coluna,sub_linha,sub_coluna = self.jogadores[atual].preparar_jogada(self.tabuleiro)
        
        while not(self.tabuleiro.definir_sub_posicao(linha, coluna, sub_linha, sub_coluna, atual)):
            pass

        id_jogador = self.tabuleiro.receber_vencedor()
        if id_jogador != None: self.finalizar()