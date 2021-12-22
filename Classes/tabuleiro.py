from typing import List
from Modulos.auxiliar import ind_pos, pos_ind

'''
- jogador_vencedor será o index do jogador na lista presente em partida
- posicoes é uma lista que pode conter tabuleiros menores, o index do jogador que selecionou aquela posição ou o index do vencedor
'''

class Tabuleiro:
    id_vencedor: int
    posicoes: List

    def __init__(self):
        self.id_vencedor = None
        self.posicoes = []
        for _ in range(9):
            self.posicoes.append(None)

    def __eq__(self, __o: object) -> bool:
        return False

    def receber_vencedor(self):
        return self.id_vencedor

    def verificar_vencedor(self):
        if self.id_vencedor != None: return

        # verificar linhas e colunas
        for i in range(0, 3):
            if self.receber_posicao(i,0) == self.receber_posicao(i,1) == self.receber_posicao(i,2) != -1:
                self.id_vencedor = self.receber_posicao(i,0)
            if self.receber_posicao(0,i) == self.receber_posicao(1,i) == self.receber_posicao(2,i) != -1:
                self.id_vencedor = self.receber_posicao(0,i)

        # verificar diagonal principal
        if self.receber_posicao(0,0) == self.receber_posicao(1,1) == self.receber_posicao(2,2) != -1:
            self.id_vencedor = self.receber_posicao(0,0)
        
        # verificar diagonal secundaria
        if self.receber_posicao(0,2) == self.receber_posicao(1,1) == self.receber_posicao(2,0) != -1:
            self.id_vencedor = self.receber_posicao(0,2)

        # verificar se deu velha
        for i in range(9):
            linha,coluna = ind_pos(i)
            if self.receber_posicao(linha,coluna) == -1 or self.ha_subtab(linha,coluna): return

        if self.id_vencedor == None: self.id_vencedor = 2


    def ha_subtab(self, linha, coluna):
        return type(self.receber_posicao(linha, coluna)).__name__ == "SubTabuleiro"

    def definir_posicao(self, linha, coluna, id):
        if self.verificar_posicao(linha, coluna):
            self.posicoes[pos_ind(linha,coluna)] = id
            self.verificar_vencedor()
            return
        return False

    def receber_posicao(self, linha, coluna):
        if self.limites(linha, coluna):
            return self.posicoes[pos_ind(linha,coluna)]

    def limites(self, linha, coluna):
        if type(linha) != int or type(linha) != int: return False
        if not(0 <= linha <= 2 and 0 <= coluna <= 2): return False
        return True