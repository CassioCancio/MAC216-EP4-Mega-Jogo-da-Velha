from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class Humano(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        linha = coluna = None
        print("• Escolha do subtabuleiro")
        while(not tabuleiro.verificar_posicao(linha, coluna)):
            if linha != None: print("Tabuleiro inválido.")
            linha = int(input("Linha (1-3): ")) - 1
            coluna = int(input("Coluna (1-3): ")) - 1

        # Verifica se a posição do subtabuleiro escolhido é válida
        sub_tabuleiro = tabuleiro.receber_posicao(linha,coluna)

        sub_linha = sub_coluna = None
        print("• Escolha da posição no subtabuleiro")
        while(not sub_tabuleiro.verificar_posicao(sub_linha, sub_coluna)):
            if sub_linha != None: print("Tabuleiro inválido.")
            sub_linha = int(input("Linha (1-3): ")) - 1
            sub_coluna = int(input("Coluna (1-3): ")) - 1

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna