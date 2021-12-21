from typing import List
from Modulos.auxiliar import pos_ind

'''
- jogador_vencedor será o index do jogador na lista presente em partida
- posicoes é uma lista que pode conter tabuleiros menores, o index do jogador que selecionou aquela posição ou o index do vencedor

'''

class Tabuleiro:
    jogador_vencedor: int
    posicoes: List

    def __init__(self):
        self.jogador_vencedor = None
        lista = []
        for _ in range(9):
            lista.append(None)
        self.posicoes = lista

    def receber_vencedor(self):
        return self.jogador_vencedor

    def verificar_vencedor(self):
        if self.jogador_vencedor != None: return

        # verificar linhas
        for i in range(0, 3):
            jogador_1 = jogador_2 = 0
            for j in range(0, 3):
                if self.posicoes[pos_ind(i,j)] == 0:
                    jogador_1 += 1
                elif self.posicoes[pos_ind(i,j)] == 1:
                    jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return
        
        # verificar colunas
        for j in range(0, 3):
            jogador_1 = jogador_2 = 0
            for i in range(0, 3):
                if self.posicoes[pos_ind(i,j)] == 0:
                    jogador_1 += 1
                elif self.posicoes[pos_ind(i,j)] == 1:
                    jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return

        # verificar diagonal principal
        jogador_1 = 0
        jogador_2 = 0
        for i in range(0, 3):
            if self.posicoes[pos_ind(i,i)] == 0:
                jogador_1 += 1
            elif self.posicoes[pos_ind(i,i)] == 1:
                jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return
        
        # verificar diagonal secundaria
        jogador_1 = 0
        jogador_2 = 0
        for i in range(1, 4):
            if self.posicoes[pos_ind(i,-i)] == 0:
                jogador_1 += 1
            elif self.posicoes[pos_ind(i,-i)] == 1:
                jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        # verificar se deu velha
        for i in range(9):
            if self.posicoes[i] == -1 or type(self.posicoes[i]).__name__ == "SubTabuleiro": 
                return

        if self.jogador_vencedor == None: 
            self.jogador_vencedor = 2

    def definir_posicao(self, linha, coluna, id):
        if self.verificar_posicao(linha, coluna):
            self.posicoes[pos_ind(linha,coluna)] = id
            self.verificar_vencedor()
            return
        return False

    def receber_posicao(self, linha, coluna):
        return self.posicoes[pos_ind(linha,coluna)]