import sys

sys.path.insert(0,'C:/Users/cassi/OneDrive/USP/2° Semestre/MAC0216/EP4 - Mega Jogo da Velha/MAC216-EP4-Mega-Jogo-da-Velha/Classes')

# from Classes.sub_tabuleiro import SubTabuleiro
from mega_tabuleiro import MegaTabuleiro

# sub = SubTabuleiro()

# for i in range(3):
#     for j in range(3):
#         print(sub.posicoes[i*3+j], end=" ")
#     print()

# sub.definir_posicao(0,3,0)

# for i in range(3):
#     for j in range(3):
#         print(sub.posicoes[i*3+j], end=" ")
#     print()


self = MegaTabuleiro()

print(type(self.posicoes[0]).__name__ == "SubTabuleiro")