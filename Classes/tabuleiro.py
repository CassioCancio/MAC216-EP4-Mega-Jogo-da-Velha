from typing import List

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
            jogador_1 = 0
            jogador_2 = 0
            for j in range(0, 3):
                if self.posicoes[i*3+j] == 0:
                    jogador_1 += 1
                elif self.posicoes[i*3+j] == 1:
                    jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return
        
        # verificar colunas
        for j in range(0, 3):
            jogador_1 = 0
            jogador_2 = 0
            for i in range(0, 3):
                if self.posicoes[j+3*i] == 0:
                    jogador_1 += 1
                elif self.posicoes[j+3*i] == 1:
                    jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return

        # verificar diagonal principal
        for i in range(0, 3):
            jogador_1 = 0
            jogador_2 = 0
            if self.posicoes[i+i*3] == 0:
                jogador_1 += 1
            elif self.posicoes[i+i*3] == 1:
                jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        if self.jogador_vencedor != None: return
        
        # verificar diagonal secundaria
        for i in range(0, 3):
            jogador_1 = 0
            jogador_2 = 0
            if self.posicoes[3*i-i] == 0:
                jogador_1 += 1
            elif self.posicoes[3*i-i] == 1:
                jogador_2 += 1
            if jogador_1 == 3:
                self.jogador_vencedor = 0
            elif jogador_2 == 3:
                self.jogador_vencedor = 1

        # verificar se deu velha
        cheio = True
        for i in range(9):
            if self.posicoes[i] != None: 
                cheio = False
        if cheio and self.jogador_vencedor == None: 
            self.jogador_vencedor = -1

    def definir_posicao(self, linha, coluna, id):
        if self.verificar_posicao(linha, coluna):
            self.posicoes[linha*3+coluna] = id
            return
        return False