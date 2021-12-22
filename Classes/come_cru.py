from jogador import Jogador
from mega_tabuleiro import MegaTabuleiro
from Modulos.auxiliar import ind_pos

class ComeCru(Jogador):
    def __init__(self, nome: str, simbolo: str):
        Jogador.__init__(self, nome, simbolo)


    def preparar_jogada(self, tabuleiro: MegaTabuleiro) -> tuple():
        ''' Busca o primeiro tabuleiro livre e depois a sua primeira posição livre para então retornar as coordenadas dessa posição '''
        # Encontrando primeiro tabuleiro livre
        for i in range(9):
            linha,coluna = ind_pos(i)
            if tabuleiro.ha_subtab(linha,coluna): break

        # Guardar subtabuleiro selecionado
        sub_tabuleiro = tabuleiro.receber_posicao(linha,coluna)

        # Encontrando primeira posição do primeiro tabuleiro livre
        for i in range(9):
            sub_linha,sub_coluna = ind_pos(i)
            if sub_tabuleiro.verificar_posicao(sub_linha,sub_coluna): break

        self.esperar()

        # Retorna o subtabuleiro escolhido e a posição escolhida para a jogada
        return linha, coluna, sub_linha, sub_coluna