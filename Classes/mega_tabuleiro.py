from tabuleiro import Tabuleiro
from sub_tabuleiro import SubTabuleiro
from Módulos.auxiliar import pos_ind, ind_pos

class MegaTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            linha, coluna = ind_pos(i)
            sub_tabuleiro = SubTabuleiro()
            self.definir_posicao(linha, coluna, sub_tabuleiro)

    def verificar_posicao(self, linha, coluna):
        if not(0 <= linha <= 3 and 0 <= coluna <= 3): return False
        if self.receber_posicao(linha, coluna) != 0 and self.receber_posicao(linha, coluna) != 1: return True
        return False

    def definir_sub_posicao(self, linha, coluna, linha_sub, coluna_sub, id):
        if type(self.receber_posicao(linha, coluna)).__name__ == "SubTabuleiro":
            self.receber_posicao(linha, coluna).definir_posicao(linha_sub, coluna_sub, id)
            return True

        print("Nessa posição não há um tabuleiro")
        return False