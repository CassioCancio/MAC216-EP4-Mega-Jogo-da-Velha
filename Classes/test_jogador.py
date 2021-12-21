import pytest
from jogador import Jogador

@pytest.fixture
def jogador_string():
    return Jogador("lorem ipsum", "s")

@pytest.fixture
def jogador_numero():
    return Jogador(12133, 12)

@pytest.fixture
def jogador_vazio():
    return Jogador("","")

class TestaJogador:
    def test_nome_letras(self, jogador_string):
        assert jogador_string.receber_nome() == "lorem ipsum"

    def test_nome_vazio(self, jogador_vazio):
        assert jogador_vazio.receber_nome() == ""

    def test_nome_numero(self, jogador_numero):
        assert jogador_numero.receber_nome() == 12133

    def test_simbolo_letra(self, jogador_string):
        assert jogador_string.receber_simbolo() == "s"

    def test_simbolo_vazio(self, jogador_vazio):
        assert jogador_vazio.receber_simbolo() == ""

    def test_simbolo_numero(self, jogador_numero):
        assert jogador_numero.receber_simbolo() == 12