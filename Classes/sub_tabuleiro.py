from tabuleiro import Tabuleiro
from Modulos.auxiliar import ind_pos

class SubTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            linha, coluna = ind_pos(i)
            self.definir_posicao(linha, coluna, -1)


    def verificar_posicao(self, linha: int, coluna: int) -> bool:
        if self.limites(linha,coluna):
            posicao = self.receber_posicao(linha,coluna)
            if posicao == None or posicao == -1: return True
        return False