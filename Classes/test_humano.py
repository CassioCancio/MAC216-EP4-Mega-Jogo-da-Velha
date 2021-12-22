import pytest
from humano import Humano
from mega_tabuleiro import MegaTabuleiro
import sys

@pytest.fixture
def humano():
    return Humano("Humano", 1)

@pytest.fixture
def mega_tabuleiro():
    return MegaTabuleiro()

class TestaHumano:
    def test_construtor_nome(self, humano):
        assert humano.receber_nome() == "Humano"

    def test_construtor_simbolo(self, humano):
        assert humano.receber_simbolo() == 1

    def test_preparar_jogada(self,humano,mega_tabuleiro):
        try:
            sys.stdin = open("./Classes/test_humano.txt")
        except:
            sys.stdin = open("./test_humano.txt")
        linha,coluna,sub_linha,sub_coluna = humano.preparar_jogada(mega_tabuleiro)
        assert linha == 0
        assert coluna == 2
        assert sub_linha == 1
        assert sub_coluna == 1