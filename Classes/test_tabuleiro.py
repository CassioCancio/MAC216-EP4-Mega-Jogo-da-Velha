from tabuleiro import Tabuleiro
from Modulos.auxiliar import pos_ind, ind_pos

import pytest
@pytest.fixture

def tabuleiro():
    return Tabuleiro()

class TestaTabuleiro():
    
    def teste_igualdade(self, tabuleiro):
        assert (tabuleiro == Tabuleiro()) == False

    def teste_vencedor(self, tabuleiro):
        assert tabuleiro.receber_vencedor() == None
    