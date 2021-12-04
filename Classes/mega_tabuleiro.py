from tabuleiro import Tabuleiro
from sub_tabuleiro import SubTabuleiro

class MegaTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            self.posicoes[i] = SubTabuleiro()

    def verificar_posicao(self, linha, coluna):
        if not(0 <= linha <= 3 and 0 <= coluna <= 3): return False
        if self.posicoes[linha*3+coluna] != 0 and self.posicoes[linha*3+coluna] != 1: return True
        return False

    def definir_posicao(self, linha, coluna, id):
        if self.verificar_posicao(linha, coluna):
            self.posicoes[linha*3+coluna] = id
            return
        return False