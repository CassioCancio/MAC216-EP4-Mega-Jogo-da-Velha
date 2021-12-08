from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro

class Humano(Jogador):
    def __init__(self):
        Jogador.__init__()

    def preparar_jogada(self, tabuleiro: MegaTabuleiro):
        # Verifica se o subtabuleiro escolhido é válido
        print("• Escolha do subtabuleiro")
        tabuleiro_linha = input("Digite a linha do tabuleiro: ")
        tabuleiro_coluna = input("Digite a coluna do tabuleiro: ")
        while(not tabuleiro.verificar_posicao(tabuleiro_linha, tabuleiro_coluna)):
            print("Tabuleiro inválido.")
            tabuleiro_linha = input("Digite a linha do tabuleiro: ")
            tabuleiro_coluna = input("Digite a coluna do tabuleiro: ")

        # Verifica se a posição do subtabuleiro escolhido é válida
        sub_tabuleiro = tabuleiro.posicoes[tabuleiro_linha*3+tabuleiro_coluna]
        print("• Escolha da posição no subtabuleiro")
        sub_linha = input("Digite a linha do subtabuleiro: ")
        sub_coluna = input("Digite a coluna do subtabuleiro: ")
        while(not sub_tabuleiro.verificar_posicao(sub_linha, sub_coluna)):
            print("Posição inválida.")
            sub_linha = input("Digite a linha do subtabuleiro: ")
            sub_coluna = input("Digite a coluna do subtabuleiro: ")

        # Se não achar posição disponível
        if sub_tabuleiro == None:
            pass # toDo

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return sub_tabuleiro, sub_linha, sub_coluna