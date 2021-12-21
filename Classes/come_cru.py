from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import ind_pos

class ComeCru(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Encontrando primeiro tabuleiro livre
        sub_tabuleiro = None
        id = 0
        for i in range(9):
            if(type(tabuleiro.posicoes[i]).__name__ == "SubTabuleiro" and tabuleiro.posicoes[i].jogador_vencedor == None):
                id = i
                break
        
        # Encontrando primeira posição do primeiro tabuleiro livre
        posicao = None
        for i in range(9):
            if(tabuleiro.posicoes[id].posicoes[i] == -1):
                posicao = i
                break
        
        # Cálculo da linha e coluna
        sub_linha, sub_coluna = ind_pos(posicao)

        linha,coluna = ind_pos(id)

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna