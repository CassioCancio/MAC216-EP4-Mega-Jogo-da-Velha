from typing import List
from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from humano import Humano
from estabanado import Estabanado
from come_cru import ComeCru
from ia import IA

class Partida:
    emAndamento: bool
    jogadores: List
    tabuleiro: MegaTabuleiro


    def __init__(self, tipo_jogador_1: int, tipo_jogador_2: int):
        self.emAndamento = True
        self.tabuleiro = MegaTabuleiro()
        self.jogadores = []
        self.jogadores.append(self.seletor_jogador(tipo_jogador_1, 1, 'x'))
        self.jogadores.append(self.seletor_jogador(tipo_jogador_2, 2, '○'))


    def fazer_jogada(self) -> None:
        atual = self.proximo_jogador()
        print(f"É a vez de {self.receber_nome_jogador(atual)} ({self.receber_simbolo_jogador(atual)})")
        linha,coluna,sub_linha,sub_coluna = self.receber_jogador(atual).preparar_jogada(self.receber_tabuleiro())
        while not(self.receber_tabuleiro().definir_sub_posicao(linha, coluna, sub_linha, sub_coluna, atual)):
            linha,coluna,sub_linha,sub_coluna = self.receber_jogador(atual).preparar_jogada(self.receber_tabuleiro())
        if self.receber_tabuleiro().receber_vencedor() != None: self.finalizar()


    def finalizar(self) -> None:
        self.emAndamento = False


    def imprimir_estado(self) -> None:
        simbolos = []
        simbolos.append(self.receber_simbolo_jogador(0))
        simbolos.append(self.receber_simbolo_jogador(1))
        simbolos.append("-")
        simbolos.append(" ")

        vert = "║"; hori = "═"; div = "╬";
        esq_sup = "╔"; esq_inf = "╚"; dir_sup = "╗"; dir_inf = "╝"
        div_esq = "╠"; div_dir = "╣"; div_inf = "╩"; div_sup = "╦"
        sub_vert = "│"; sub_hori = "─"; sub_div = "┼"
        antes = f"{vert}   "
        depois = f"   {vert}"

        print(f"{esq_sup + hori*43 + dir_sup }")
        print(f"{antes}{' '*6}1{' '*11}2{' '*11}3{' '*6}{depois}")
        print(f"{antes}{esq_sup + hori*11 + div_sup + hori*11 + div_sup + hori*11 + dir_sup }{depois}")
        for linha in range(3):
            for sub_linha in range(3):
                if sub_linha == 1: print(f'{vert} {linha+1} ', end="")
                else: print(f'{antes}', end="")
                for coluna in range(3):
                    if coluna == 0: print(vert, end="")
                    for sub_coluna in range(3):
                        print(f' {simbolos[self.receber_tabuleiro().receber_sub_posicao(linha,coluna,sub_linha,sub_coluna)]} ', end="")
                        if sub_coluna < 2: print(sub_vert, end="")
                    print(vert, end="")
                    if coluna == 2:
                        if sub_linha == 1: print(f' {linha+1} {vert}',end="")
                        else: print(depois,end="")
                if sub_linha < 2: print(f"\n{antes}{vert+((((sub_hori*3+sub_div)*3)[0:11]+vert)*3)[0:35]+vert}{depois}",end="")
                print()
            if linha < 2: print(f"{antes}{div_esq+((hori*11+div)*3)[0:35]+div_dir}{depois}")
        print(f"{antes}{esq_inf + hori*11 + div_inf + hori*11 + div_inf + hori*11 + dir_inf}{depois}")
        print(f"{antes}{' '*6}1{' '*11}2{' '*11}3{' '*6}{depois}")
        print(f"{esq_inf + hori*43 + dir_inf }")
        print()


    def receber_andamento(self) -> bool:
        return self.emAndamento


    def receber_jogador(self, id) -> Jogador:
        if id != None and 0 <= id <= 1: return self.jogadores[id]


    def receber_nome_jogador(self, id) -> str:
        return self.jogadores[id].receber_nome()


    def receber_simbolo_jogador(self, id) -> str:
        return self.jogadores[id].receber_simbolo()


    def receber_tabuleiro(self) -> MegaTabuleiro:
        return self.tabuleiro


    def receber_vencedor(self) -> Jogador:
        return self.receber_jogador(self.receber_tabuleiro().receber_vencedor())


    def seletor_jogador(self, tipo: int, id: int, simbolo: str) -> Jogador:
        if tipo == 1: return Humano(f"Humano {id}", simbolo)
        if tipo == 2: return Estabanado(f"Estabanado {id}", simbolo)
        if tipo == 3: return ComeCru(f"Come cru {id}", simbolo)
        if tipo == 4: return IA(f"IA {id}", simbolo)
        return None