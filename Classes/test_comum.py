from comum import Comum
from humano import Humano
from estabanado import Estabanado
from come_cru import ComeCru
from ia import IA
from Modulos.auxiliar import pos_ind, ind_pos

import pytest
@pytest.fixture

def comum():
    return Comum(2,0)

class TestaComum():
    def teste_proximo(self, comum):
        assert comum.proximo_jogador() == 0
        assert comum.proximo_jogador() == 1
        assert comum.proximo_jogador() == 0
        
    def test_tipo_humano(self,comum):
        assert type(comum.receber_jogador(1)) == Humano

    def test_tipo_estabanado(self):
        comum = Comum(1,1)
        assert type(comum.receber_jogador(0)) == Estabanado
    
    def test_tipo_come_cru(self,comum):
        assert type(comum.receber_jogador(0)) == ComeCru
    
    def test_tipo_ia(self):
        comum = Comum(3,3)
        assert type(comum.receber_jogador(0)) == IA

    def test_id_jogador_invalido(self):
        comum = Comum(4,4)
        assert comum.receber_jogador(0) == None

    def test_andamento(self,comum):
        assert comum.receber_andamento() == True
    
    def teste_fazer_jogada(self,comum):
        assert comum.receber_tabuleiro().receber_sub_posicao(0,0,0,0) == -1
        comum.fazer_jogada()
        assert comum.receber_tabuleiro().receber_sub_posicao(0,0,0,0) == 0