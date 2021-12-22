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
        ''' Abre o subtabuleiro dado pela coordenada linha x coluna e coloca o valor dado na posição sub_linha x sub_coluna desse subtabuleiro '''
        # Verifica se há tabuleiro naquela posição
        if self.ha_subtab(linha,coluna):

            # Guardar subtabuleiro dado
            sub_tab = self.receber_posicao(linha, coluna)

            # Defini sua posição
            sub_tab.definir_posicao(sub_linha, sub_coluna, id)

            # Verifica se ele já foi definido, ou seja, se alguém venceu ou deu velha
            if sub_tab.receber_vencedor() != None: self.definir_posicao(linha,coluna,id)

            return True
        print("Nessa posição não há um tabuleiro")
        return False


    def receber_sub_posicao(self, linha: int, coluna: int, sub_linha: int, sub_coluna: int) -> int:
        ''' Abre o subtabuleiro dado pela coordenada linha x coluna e pega o valor da posição sub_linha x sub_coluna desse subtabuleiro '''
        # Verifica se os números estão dentro dos limites exigidos
        if self.limites(linha, coluna):

            # Verifica se há subtabuleiro nessa posição
            if self.ha_subtab(linha,coluna):
                return self.receber_posicao(linha,coluna).receber_posicao(sub_linha,sub_coluna)
        
            #  Se não houver, retorne o valor da casa
            return self.receber_posicao(linha,coluna)
        return None


    def verificar_posicao(self, linha: int, coluna: int) -> bool:
        ''' Verifica se a posição dada é válida e se há um número nessa posição, se não houver, a posição ainda tem um tabuleiro '''
        # Verifica se os números estão dentro dos limites exigidos
        if self.limites(linha,coluna):

            # Verifica se não há um número naquela causa, ou seja, ainda pode ser marcada
            posicao = self.receber_posicao(linha, coluna)
            if type(posicao) != int: return True

        return False

    def conta_jogadas(self, id: int, linha: int, coluna: int) -> bool:
        ''' Conta o número de casas marcadas com um id e diz se há mais dele ou do outro id no subtabuleiro dado '''
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