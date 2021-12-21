from sub_tabuleiro import SubTabuleiro
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import ind_pos

class ComeCru(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Encontrando primeiro tabuleiro livre
        for i in range(9):
            linha,coluna = ind_pos(i)
            if tabuleiro.ha_subtab(linha,coluna): break

        sub_tabuleiro = tabuleiro.receber_posicao(linha,coluna)

        # Encontrando primeira posição do primeiro tabuleiro livre
        for i in range(9):
            sub_linha,sub_coluna = ind_pos(i)
            if sub_tabuleiro.verificar_posicao(sub_linha,sub_coluna): break
        
        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna