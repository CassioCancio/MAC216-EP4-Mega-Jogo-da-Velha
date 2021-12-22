from tabuleiro import Tabuleiro
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class IA(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro:MegaTabuleiro):
        linha = coluna = sub_linha = sub_coluna = id = None
        if(self.simbolo == 'x'):
            id = 1
        else:
            id = 2

        # Encontra o subtabuleiro correto
        for i in range(0, 3):
            for j in range(0, 3):
                if(tabuleiro.conta_jogadas(id, i, j)):
                    linha = i
                    coluna = j
                    break

        if(linha == None):
            linha = coluna = 0

        # Se não houver jogada no meio, jogue nessa posição
        posicao_central = tabuleiro.receber_sub_posicao(linha, coluna, 1, 1)
        if(posicao_central == -1):
            return linha, coluna, 1, 1

        # Se o adversário jogar nos cantos centrais ou no meio jogue nas diagonais ou no canto central oposto
        canto_esquerdo_meio = tabuleiro.receber_sub_posicao(linha, coluna, 1, 0)
        canto_cima_meio = tabuleiro.receber_sub_posicao(linha, coluna, 0, 1)
        canto_direito_meio = tabuleiro.receber_sub_posicao(linha, coluna, 1, 2)
        canto_baixo_meio = tabuleiro.receber_sub_posicao(linha, coluna, 2, 1)
        if(canto_baixo_meio not in [-1, id] or canto_cima_meio not in [-1, id]\
            or canto_direito_meio not in [-1, id] or canto_esquerdo_meio not in [-1, id] or posicao_central != -1):
            if(tabuleiro.receber_sub_posicao(linha, coluna, 0, 0) == -1):
                return linha, coluna, 0, 0
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 0, 2) == -1):
                return linha, coluna, 0, 2
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 2, 0) == -1):
                return linha, coluna, 2, 0
            elif(tabuleiro.receber_sub_posicao(linha, coluna, 2, 2) == -1):
                return linha, coluna, 2, 2

        # Se o adversário jogar nas diagonais 
            # #toDo

        self.esperar()