from tabuleiro import Tabuleiro

class SubTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            self.posicoes[i] = -1
    
    def verificar_posicao(self, linha, coluna) -> bool:
        if not(0 <= linha <= 3 and 0 <= coluna <= 3): return False
        if self.posicoes[linha*3+coluna] == -1: return True
        return False



