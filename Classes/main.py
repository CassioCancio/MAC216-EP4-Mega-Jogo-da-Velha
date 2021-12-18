
from aleatoria import Aleatoria
from comum import Comum

def main():
    print("Bem-vindo ao MEGA JOGO DA VELHA")

    while True:
        modo = int(input(f"Insira o ID do modo de jogo:\n(0) Normal     (1) Aleatório\n")) 
        if 0 <= modo <= 1: break
        print("Número Inválido")
    print()

    tipos = []
    while len(tipos) < 2:
        tipo_dado = int(input(f"Insira o tipo do {len(tipos)+1}° jogador:\n(0) Humano     (1) Estabanado     (2) Come Cru     (3) IA\n"))
        if (0 <= tipo_dado <= 3):
            tipos.append(tipo_dado)
            continue
        print("Número Inválido")
    print()


    if modo == 0: partida = Comum(tipos[0], tipos[1])
    if modo == 1: partida = Aleatoria(tipos[0], tipos[1])


    while partida.receber_andamento():
        partida.fazer_jogada()
        partida.imprimir_estado()

    jogador_vencedor = partida.receber_vencedor()

    if jogador_vencedor == None:
        print("O JOGO DEU VELHA!")
    else:
        print(f"O JOGADOR VENCEDOR FOI {jogador_vencedor.receber_nome()}")



if __name__ == "__main__":
    main()