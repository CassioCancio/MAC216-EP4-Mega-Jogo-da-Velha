from partida import Partida

import pytest
@pytest.fixture

def partida():
    return Partida(3,1)

class TestaPartida():
    def teste_receber_vencedor(self, partida):
        assert partida.receber_vencedor() == None
    
    def teste_receber_nome_jogador(self,partida):
        assert partida.receber_nome_jogador(0) == "Come cru 1"
        assert partida.receber_nome_jogador(1) == "Humano 2"

    def teste_receber_simbolo_jogador(self,partida):
        assert partida.receber_simbolo_jogador(0) == "x"
        assert partida.receber_simbolo_jogador(1) == "○"
    
    def teste_finalizar(self, partida):
        partida.finalizar()
        assert partida.receber_andamento() == False

    def teste_imprimir(self,partida):
        assert partida.imprimir_estado() == None