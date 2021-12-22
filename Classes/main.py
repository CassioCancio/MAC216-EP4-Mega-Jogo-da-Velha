
from aleatoria import Aleatoria
from comum import Comum

def main():
    print("Bem-vindo ao MEGA JOGO DA VELHA")

    while True:
        modo = int(input(f"Insira o ID do modo de jogo:\n(1) Normal     (2) Aleatório\n")) 
        if 1 <= modo <= 2: break
        print("Número Inválido")
    print()

    tipos = []
    while len(tipos) < 2:
        tipo_dado = int(input(f"Insira o tipo do {len(tipos)+1}° jogador:\n(1) Humano     (2) Estabanado     (3) Come Cru     (4) IA\n"))
        if 1 <= tipo_dado <= 4:
            tipos.append(tipo_dado)
            continue
        print("Número Inválido")
    print()

    if modo == 1: partida = Comum(tipos[0], tipos[1])
    if modo == 2: partida = Aleatoria(tipos[0], tipos[1])

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