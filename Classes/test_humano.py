import pytest
from humano import Humano

@pytest.fixture
def humano():
    return Humano("Humano", 1)

class TestaHumano:
    def test_construtor_nome(self, humano):
        assert humano.receber_nome() == "Humano"

    def test_construtor_simbolo(self, humano):
        assert humano.receber_simbolo() == 1