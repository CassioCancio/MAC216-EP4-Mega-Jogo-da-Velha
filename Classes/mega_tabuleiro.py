from tabuleiro import Tabuleiro
from sub_tabuleiro import SubTabuleiro
from Modulos.auxiliar import ind_pos

class MegaTabuleiro(Tabuleiro):
    def __init__(self):
        Tabuleiro.__init__(self)
        for i in range(9):
            linha,coluna = ind_pos(i)
            sub_tabuleiro = SubTabuleiro()
            self.definir_posicao(linha, coluna, sub_tabuleiro)


    def definir_sub_posicao(self, linha: int, coluna: int, sub_linha: int, sub_coluna: int, id: int) -> bool:
        if self.ha_subtab(linha,coluna):
            sub_tab = self.receber_posicao(linha, coluna)
            sub_tab.definir_posicao(sub_linha, sub_coluna, id)
            if sub_tab.receber_vencedor() != None: self.definir_posicao(linha,coluna,id)
            return True
        print("Nessa posição não há um tabuleiro")
        return False


    def receber_sub_posicao(self, linha: int, coluna: int, sub_linha: int, sub_coluna: int) -> int:
        if self.limites(linha, coluna):
            if self.ha_subtab(linha,coluna):
                return self.receber_posicao(linha,coluna).receber_posicao(sub_linha,sub_coluna)
            return self.receber_posicao(linha,coluna)
        return None


    def verificar_posicao(self, linha: int, coluna: int) -> bool:
        if self.limites(linha,coluna):
            posicao = self.receber_posicao(linha, coluna)
            if type(posicao) != int: return True
        return False

    def conta_jogadas(self, linha, coluna, id):
        contador_um = 0
        contador_dois = 0

        for i in range(0, 3):
            for j in range(0, 3):
                celula = self.receber_sub_posicao(linha, coluna, i, j)
                if(celula == id):
                    contador_um += 1
                elif(celula != -1):
                    contador_dois += 1

        if(contador_um < contador_dois):
            return True
        else:
            return False