from tabuleiro import Tabuleiro
from Modulos.auxiliar import pos_ind, ind_pos

class SubTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            linha, coluna = ind_pos(i)
            self.definir_posicao(linha, coluna, -1)

    def verificar_posicao(self, linha, coluna) -> bool:
        if not(0 <= linha <= 3 and 0 <= coluna <= 3): return False
        if self.posicoes[pos_ind(linha, coluna)] == None: return True
        if self.posicoes[pos_ind(linha,coluna)] == -1: return True
        return False