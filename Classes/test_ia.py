import pytest
from ia import IA
from mega_tabuleiro import MegaTabuleiro

@pytest.fixture
def ia():
    return IA("Nome", 'x')

@pytest.fixture
def mega_tabuleiro():
    return MegaTabuleiro()

class TestaIA():
    def test_construtor_nome(self, ia):
        assert ia.receber_nome() == "Nome"
    
    def test_construtor_simbolo(self, ia):
        assert ia.receber_simbolo() == 'x'

    def test_preparar_jogada(self, ia, mega_tabuleiro):
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1

    def test_preparar_jogada_meio_ocupado(self, ia, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 1, 1, 1)
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1

    def test_preparar_jogada_meio_esquerda_superior_ocupadas(self, ia, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 1, 1, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1
    
    def test_preparar_jogada_meio_direita_superior_ocupadas(self, ia, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 1, 1, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 2, 1)
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1

    def test_preparar_jogada_meio_esquerda_inferior_ocupadas(self, ia, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 1, 1, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 2, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 2, 0, 2)
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1
    
    def test_preparar_jogada_meio_direita_inferior_ocupadas(self, ia, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 1, 1, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 2, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 2, 0, 2)
        mega_tabuleiro.definir_sub_posicao(0, 0, 2, 2, 2)
        linha, coluna, sub_linha, sub_coluna = ia.preparar_jogada(mega_tabuleiro)
        assert mega_tabuleiro.receber_sub_posicao(linha, coluna, sub_linha, sub_coluna) == -1