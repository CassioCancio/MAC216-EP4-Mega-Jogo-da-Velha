def pos_ind (linha, colunas):
    return linha*3+colunas

def ind_pos (indice):
    return (indice // 3, indice % 3)