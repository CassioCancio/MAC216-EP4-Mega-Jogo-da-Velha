from random import randint
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import ind_pos

class Estabanado(Jogador):
    def __init__(self, nome: str, simbolo: str):
        Jogador.__init__(self, nome, simbolo)


    def preparar_jogada(self, tabuleiro: MegaTabuleiro) -> tuple():
        ''' Busca o aleatóriamente um tabuleiro livre e depois sorteia uma posição livre dentro dele para então retornar as coordenadas dessa posição '''
        # Sorteando tabuleiro livre
        sub_indices = list(range(9))
        linha = coluna = None
        for i in range(9):
            sorte = randint(i, 8)
            linha,coluna = ind_pos(sub_indices[sorte])
            if(tabuleiro.ha_subtab(linha, coluna)): break
            sub_indices[i], sub_indices[sorte] = sub_indices[sorte], sub_indices[i]

        # Guardar subtabuleiro sorteado
        sub_tabuleiro = tabuleiro.receber_posicao(linha,coluna)

        # Sorteando posição livre no tabuleiro
        pos_indices = list(range(9))
        sub_linha = sub_coluna = None
        for i in range(9):
            sorte = randint(i, 8)
            sub_linha, sub_coluna = ind_pos(pos_indices[sorte])
            if(sub_tabuleiro.verificar_posicao(sub_linha, sub_coluna)): break
            pos_indices[i], pos_indices[sorte] = pos_indices[sorte], pos_indices[i]

        self.esperar()

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna