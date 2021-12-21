from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import pos_ind

class Humano(Jogador):
    def __init__(self, nome, simbolo):
        Jogador.__init__(self, nome, simbolo)

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Verifica se o subtabuleiro escolhido é válido
        print("• Escolha do subtabuleiro")
        tabuleiro_linha = int(input("Digite a linha do tabuleiro: "))
        tabuleiro_coluna = int(input("Digite a coluna do tabuleiro: "))
        while(not tabuleiro.verificar_posicao(tabuleiro_linha, tabuleiro_coluna)):
            print("Tabuleiro inválido.")
            tabuleiro_linha = int(input("Digite a linha do tabuleiro: "))
            tabuleiro_coluna = int(input("Digite a coluna do tabuleiro: "))

        # Verifica se a posição do subtabuleiro escolhido é válida
        indice = pos_ind(tabuleiro_linha, tabuleiro_coluna)
        sub_tabuleiro = tabuleiro.posicoes[indice]
        print("• Escolha da posição no subtabuleiro")
        sub_linha = int(input("Digite a linha do subtabuleiro: "))
        sub_coluna = int(input("Digite a coluna do subtabuleiro: "))
        while(not sub_tabuleiro.verificar_posicao(sub_linha, sub_coluna)):
            print("Posição inválida.")
            sub_linha = int(input("Digite a linha do subtabuleiro: "))
            sub_coluna = int(input("Digite a coluna do subtabuleiro: "))

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return tabuleiro_linha, tabuleiro_coluna, sub_linha, sub_coluna