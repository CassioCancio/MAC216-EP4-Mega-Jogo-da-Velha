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


    def definir_posicao(self, linha: int, coluna: int, id: int) -> bool:
        ''' Marca a posição dada com o valor em id '''
        if self.verificar_posicao(linha, coluna):
            self.posicoes[pos_ind(linha,coluna)] = id
            self.verificar_vencedor()
            return True
        return False


    def ha_subtab(self, linha: int, coluna: int) -> bool:
        ''' Verifica se há um subtabuleiro na posição dada '''
        return type(self.receber_posicao(linha, coluna)).__name__ == "SubTabuleiro"


    def limites(self, linha: int, coluna: int) -> bool:
        ''' Verifica se os parâmetros dados são números e se estão no intervalo [0,2]'''
        if type(linha) != int or type(linha) != int: return False
        if not(0 <= linha <= 2 and 0 <= coluna <= 2): return False
        return True


    def receber_posicao(self, linha: int, coluna: int) -> object:
        ''' Retorna o objeto presente na posição dada'''
        if self.limites(linha, coluna):
            return self.posicoes[pos_ind(linha,coluna)]


    def receber_vencedor(self) -> int:
        ''' Retorna o id do jogador vencedor'''
        return self.id_vencedor


    def verificar_vencedor(self) -> None:
        ''' Verifica se um tabuleiro já foi ganho ou se deu velha '''
        # Checa se já não há vencedor
        if self.id_vencedor != None: return

        # Verificar linhas e colunas
        for i in range(0, 3):
            if self.receber_posicao(i,0) == self.receber_posicao(i,1) == self.receber_posicao(i,2) != -1:
                self.id_vencedor = self.receber_posicao(i,0)
            if self.receber_posicao(0,i) == self.receber_posicao(1,i) == self.receber_posicao(2,i) != -1:
                self.id_vencedor = self.receber_posicao(0,i)

        # Verificar diagonal principal
        if self.receber_posicao(0,0) == self.receber_posicao(1,1) == self.receber_posicao(2,2) != -1:
            self.id_vencedor = self.receber_posicao(0,0)
        
        # Verificar diagonal secundaria
        if self.receber_posicao(0,2) == self.receber_posicao(1,1) == self.receber_posicao(2,0) != -1:
            self.id_vencedor = self.receber_posicao(0,2)

        # Verificar se não deu velha
        for i in range(9):
            linha,coluna = ind_pos(i)
            if self.receber_posicao(linha,coluna) == -1 or self.ha_subtab(linha,coluna): return

        # Se não saiu até agora, significa que deu velha
        if self.id_vencedor == None: self.id_vencedor = 2