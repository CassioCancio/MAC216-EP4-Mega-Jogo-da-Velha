'''Recebe linha e coluna e retorna um índice'''
def pos_ind (linha, colunas):
    return linha*3+colunas

'''Recebe um índice e retorna uma tupla(linha, coluna)'''
def ind_pos (indice):
    return (indice // 3, indice % 3)