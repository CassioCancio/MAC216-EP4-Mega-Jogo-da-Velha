# MAC0216 - EP4 Mega Jogo da Velha
Integrantes |nUSP
-- | --
Cássio Azevedo Cancio | 4818166 
Luiz Gabriel Lima Arrais | 12543523

Este repositório foi criado com o objetivo de registrar e armazenar o EP (Exercício Programa) de Programação Orientação a Objetos em Python, dado durante a matéria de MAC0216 em 2021 no IME-USP. O projeto consiste na produção de um Mega Jogo da Velha, no qual cada casa do tabuleiro é um tabuleiro menor, como ilustrado abaixo:

![Exemplo de mega tabuleiro](./documentacao/exemplo_mega_tabuleiro.png)

Para ganhar o jogo, o jogador precisa ganhar 3 subtabuleiros que formem uma linha reta. O programa possui dois tipos de partida:

* Comum - na qual os jogadores revezam entre as jogadas;
* Aleatória - na qual os jogadores são escolhidos aleatoriamente para jogar, o que torna o jogo mais divertido. 

Além disso, existem 4 tipos de jogadores:

* Come cru - o computador joga sempre na casa primeira casa vazia do primeiro subtabuleiro disponível;
* Estabanado - o computador sorteia uma posição e a marca
* Humano - para que uma pessoa possa digitar as posições a serem marcadas;
* IA - o computador escolhe uma posição intencionalmente para tentar vencer o jogo;


### Organização, classes e testes
Para facilitar o desenvolvimento do programa, primeiro foi criado um diagrama de classes para representar os atributos e métodos que cada classe precisaria ter. O diagrama está na imagem a seguir:

![Diagrama de classes](./documentacao/diagrama_de_classes.png)

Os testes automatizados foram criados com pytest visando cobrir a maior quantidade de casos possíveis, assim, o programa teve 99% das linhas testadas, o que ajudou a encontrar e evitar bugs. É possível rodar os testes automatizados digitando *pytest* dentro da pasta do repositório no terminal de um sistema com essa biblioteca

### Uso do programa

Para usar o programa, é necessário rodar o comando *python main.py* dentro da pasta *Classes*. Em seguida, o programa mostrará os modos disponíveis e os tipos de jogadores. Para selecionar, basta digitar o número correspondente da opção. Exemplo:

![Exemplo de configuração](./documentacao/exemplo_configuracao.png)

Caso o usuário tenha escolhido apenas jogadores operados pela máquina, o jogo se iniciará pausando por 2 segundo a cada rodada para que o usuário possa ver as jogadas sendo feitas. No caso de ser escolhido o jogador humano, o jogo pedirá ao usuário que digite as posições do subtabuleiro desejado, depois da posição dentro do subtabuleiro. Exemplo:

![Exemplo de jogador humano](./documentacao/exemplo_humano.png)

As jogadas devem ser feitas. Quando o resultado estiver determinado, o programa encerrará a execução, anunciando, se houver vencedor, quem foi e, se não houver, anunciará que o jogo deu velha. Enfim, esse é o jogo, boa diversão 🙂