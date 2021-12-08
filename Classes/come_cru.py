from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class ComeCru(Jogador):
    def __init__(self):
        Jogador.__init__()

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Encontrando primeiro tabuleiro livre
        sub_tabuleiro = None
        for sub in tabuleiro.posicoes:
            if(sub.jogador_vencedor == None):
                sub_tabuleiro = sub
                break
        
        # Encontrando primeira posição do primeiro tabuleiro livre
        posicao = None
        for pos in sub_tabuleiro.posicoes:
            if(pos == -1):
                posicao = pos
                break
        
        # Cálculo da linha e coluna
        coluna = posicao % 3
        linha = (posicao - coluna) // 3

        # Se não achar posição disponível
        if sub_tabuleiro == None:
            pass #toDo

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return sub_tabuleiro, linha, coluna