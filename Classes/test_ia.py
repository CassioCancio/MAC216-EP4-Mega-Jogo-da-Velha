import pytest
from ia import IA
from mega_tabuleiro import MegaTabuleiro

@pytest.fixture
def ia():
    return IA("Nome", 1)

@pytest.fixture
def mega_tabuleiro():
    return MegaTabuleiro()

class TestaIA():
    def test_construtor_nome(self, ia):
        assert ia.receber_nome() == "Nome"
    
    def test_construtor_simbolo(self, ia):
        assert ia.receber_simbolo() == 1

    def test_preparar_jogada(self, ia, mega_tabuleiro):
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1