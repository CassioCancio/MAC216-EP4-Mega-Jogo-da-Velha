import pytest
from estabanado import Estabanado
from mega_tabuleiro import MegaTabuleiro

@pytest.fixture
def estabanado():
    return Estabanado("Estabanado", 1)

@pytest.fixture
def mega_tabuleiro():
    return MegaTabuleiro()

class TestaEstabanado():
    def test_estabanado_construtor_nome(self, estabanado):
        assert estabanado.receber_nome() == "Estabanado"

    def test_estabanado_construtor_simbolo(self, estabanado):
        assert estabanado.receber_simbolo() == 1

    def test_estabanado_posicao_disponivel(self, estabanado, mega_tabuleiro):
        linha, coluna, sub_linha, sub_coluna = estabanado.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1
    



