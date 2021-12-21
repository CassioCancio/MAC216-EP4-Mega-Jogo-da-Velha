import pytest
from come_cru import ComeCru
from mega_tabuleiro import MegaTabuleiro

@pytest.fixture
def come_cru():
    return ComeCru("ComeCru", 1)

@pytest.fixture
def mega_tabuleiro():
    return MegaTabuleiro()

class TestaComeCru():
    def test_construtor_nome(self, come_cru):
        assert come_cru.receber_nome() == "ComeCru"

    def test_construtor_simbolo(self, come_cru):
        assert come_cru.receber_simbolo() == 1

    def test_preparar_jogada(self, come_cru, mega_tabuleiro):
        linha, coluna, sub_linha, sub_coluna = come_cru.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1
