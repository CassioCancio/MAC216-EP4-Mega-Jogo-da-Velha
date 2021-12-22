from mega_tabuleiro import SubTabuleiro
from Modulos.auxiliar import pos_ind, ind_pos

import pytest
@pytest.fixture

def sub_tabuleiro():
    return SubTabuleiro()

class TestaSubTabuleiro():
    def teste_definir_errado(self, sub_tabuleiro):
        assert sub_tabuleiro.definir_posicao(4,4,0) == False