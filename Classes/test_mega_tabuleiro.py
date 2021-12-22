from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import pos_ind, ind_pos

import pytest
@pytest.fixture

def mega_tabuleiro():
    return MegaTabuleiro()

class TestaMegaTabuleiro():
    
    def teste_tipo(self, mega_tabuleiro):
        assert type(mega_tabuleiro.receber_posicao(0,0)).__name__ == "SubTabuleiro"

    def teste_definir(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0,0,2)
        assert mega_tabuleiro.receber_posicao(0,0) == 2
    
    def teste_definir_sub(self, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0,0,1,2,7)
        assert mega_tabuleiro.receber_sub_posicao(0,0,1,2) == 7

    def teste_receber_posicao_sem_sub(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0,0,1)
        assert mega_tabuleiro.receber_sub_posicao(0,0,1,2) == 1
    
    def teste_receber_sub_posicao_invalida(self,mega_tabuleiro):
        assert mega_tabuleiro.receber_sub_posicao(3,3,3,3) == None

    def teste_verificar_invalido(self, mega_tabuleiro):
        assert mega_tabuleiro.verificar_posicao(4,4) == False

    def teste_definir_invalido(self, mega_tabuleiro):
        assert mega_tabuleiro.definir_sub_posicao(4,4,1,2,0) == False

    def teste_vencedor_diagonal_principal(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0,0,1)
        mega_tabuleiro.definir_posicao(1,1,1)
        mega_tabuleiro.definir_posicao(2,2,1)
        mega_tabuleiro.verificar_vencedor()
        assert mega_tabuleiro.receber_vencedor() == 1

    def teste_vencedor_diagonal_secundaria(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0, 2, 1)
        mega_tabuleiro.definir_posicao(1, 1, 1)
        mega_tabuleiro.definir_posicao(2, 0, 1)
        mega_tabuleiro.verificar_vencedor()
        assert mega_tabuleiro.receber_vencedor() == 1

    def teste_vencedor_linhas(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0, 0, 1)
        mega_tabuleiro.definir_posicao(0, 1, 1)
        mega_tabuleiro.definir_posicao(0, 2, 1)
        mega_tabuleiro.verificar_vencedor()
        assert mega_tabuleiro.receber_vencedor() == 1
    
    def teste_vencedor_colunas(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0, 0, 1)
        mega_tabuleiro.definir_posicao(1, 0, 1)
        mega_tabuleiro.definir_posicao(2, 0 ,1)
        mega_tabuleiro.verificar_vencedor()
        assert mega_tabuleiro.receber_vencedor() == 1

    def teste_posicao_invalida(self, mega_tabuleiro):
        assert mega_tabuleiro.receber_posicao(4,4) == None 

    def teste_velha(self, mega_tabuleiro):
        mega_tabuleiro.definir_posicao(0,0,0)
        mega_tabuleiro.definir_posicao(0,1,0)
        mega_tabuleiro.definir_posicao(0,2,1)
        mega_tabuleiro.definir_posicao(1,0,1)
        mega_tabuleiro.definir_posicao(1,1,0)
        mega_tabuleiro.definir_posicao(1,2,0)
        mega_tabuleiro.definir_posicao(2,0,0)
        mega_tabuleiro.definir_posicao(2,1,1)
        mega_tabuleiro.definir_posicao(2,2,1)
        assert mega_tabuleiro.receber_vencedor() == 2

    def teste_conta_jogadas_iguais(self, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 1, 2)
        assert mega_tabuleiro.conta_jogadas(1, 0, 0) == False

    def teste_conta_jogadas_maior(self, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 1)
        assert mega_tabuleiro.conta_jogadas(1, 0, 0) == False
        
    def teste_conta_jogadas_maior(self, mega_tabuleiro):
        mega_tabuleiro.definir_sub_posicao(0, 0, 0, 0, 2)
        assert mega_tabuleiro.conta_jogadas(1, 0, 0) == True