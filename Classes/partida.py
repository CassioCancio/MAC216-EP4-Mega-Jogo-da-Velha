from typing import List
from mega_tabuleiro import MegaTabuleiro
from humano import Humano
from estabanado import Estabanado
from come_cru import ComeCru
from ia import IA

class Partida:
    emAndamento: bool
    jogadores: List
    tabuleiro: MegaTabuleiro

    def __init__(self, jogador1, jogador2):
        self.proximo_a_jogar = 0
        self.emAndamento = True
        self.tabuleiro = MegaTabuleiro()
        self.jogadores = []
        self.jogadores.append(self.seletor_jogador(jogador1, 1, 'x'))
        self.jogadores.append(self.seletor_jogador(jogador2, 2, '○'))
    
    def seletor_jogador(self, tipo: int, id: int, simbolo: str):
        if tipo == 0: return Humano(f"Humano {id}", simbolo)
        if tipo == 1: return Estabanado(f"Estabanado {id}", simbolo)
        if tipo == 2: return ComeCru(f"Come cru {id}", simbolo)
        if tipo == 3: return IA(f"IA {id}", simbolo)
        return None

    def receber_andamento(self):
        return self.emAndamento

    def receber_vencedor(self):
        id = self.tabuleiro.receber_vencedor()
        if id != None and 0 <= id <= 1: return self.jogadores[id]
        return None

    def receber_nome_jogador(self, id):
        return self.jogadores[id].receber_nome()

    def receber_simbolo_jogador(self, id):
        return self.jogadores[id].receber_simbolo()

    def fazer_jogada(self):
        pass

    def finalizar(self):
        self.emAndamento = False

    def imprimir_estado(self):
        simbolos = []
        simbolos.append(self.receber_simbolo_jogador(0))
        simbolos.append(self.receber_simbolo_jogador(1))
        simbolos.append("-")
        simbolos.append(" ")

        vert = "║"; hori = "═"; div = "╬";
        esq_sup = "╔"; esq_inf = "╚"; dir_sup = "╗"; dir_inf = "╝"
        div_esq = "╠"; div_dir = "╣"; div_inf = "╩"; div_sup = "╦"
        sub_vert = "│"; sub_hori = "─"; sub_div = "┼"

        print(f"{esq_sup + hori*11 + div_sup + hori*11 + div_sup + hori*11 + dir_sup }")
        for linha in range(3):
            for sub_linha in range(3):
                for coluna in range(3):
                    if coluna == 0: print(vert, end="")
                    for sub_coluna in range(3):
                        print(f' {simbolos[self.tabuleiro.receber_sub_posicao(linha,coluna,sub_linha,sub_coluna)]} ', end="")
                        if sub_coluna < 2: print(sub_vert, end="")
                    if coluna < 2: print(vert, end="")
                    if coluna == 2: print(vert, end="")
                if sub_linha < 2: print(f"\n{vert+((((sub_hori*3+sub_div)*3)[0:11]+vert)*3)[0:35]+vert}")
            if linha < 2: print(f"\n{div_esq+((hori*11+div)*3)[0:35]+div_dir}")
        print()
        print(f"{esq_inf + hori*11 + div_inf + hori*11 + div_inf + hori*11 + dir_inf }")
