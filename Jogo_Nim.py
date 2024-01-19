def computador_escolhe_jogada(n, m):
    # Estratégia vencedora: deixar múltiplos de (m+1) peças ao jogador
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)

def usuario_escolhe_jogada(n, m):
    while True:
        try:
            jogada = int(input(f'Quantas peças você vai tirar (1-{m}): '))
            if 1 <= jogada <= m and jogada <= n:
                return jogada
            else:
                print(f'Oops! Jogada inválida! Tente de novo.')
        except ValueError:
            print('Oops! Jogada inválida! Tente de novo.')

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    vez_do_pc = n % (m + 1) != 0

    if vez_do_pc:
        print("\nComputador começa!\n")
    else:
        print("\nVocê começa!\n")

    while n > 0:
        if vez_do_pc:
            jogada = computador_escolhe_jogada(n, m)
            print(f'O computador tirou {jogada} peça{"s" if jogada > 1 else ""}.')
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f'Você tirou {jogada} peça{"s" if jogada > 1 else ""}.')

        n -= jogada

        if n == 1:
            print('\nAgora resta apenas uma peça no tabuleiro.\n')
        elif n > 1:
            print(f'\nAgora restam {n} peças no tabuleiro.\n')

        vez_do_pc = not vez_do_pc

    if not vez_do_pc:  # Corrigido aqui
        print('Fim do jogo! O computador ganhou!\n')
        return 0
    else:
        print('Fim do jogo! Você ganhou!\n')
        return 1

def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print(f'\n**** Rodada {rodada} ****\n')
        resultado = partida()

        if resultado == 0:
            placar_computador += 1
        else:
            placar_usuario += 1

    print('\n**** Final do campeonato! ****\n')
    print(f'Placar: Você {placar_usuario} X {placar_computador} Computador')

if __name__ == "__main__":
    print("Bem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato")

    escolha = int(input())

    if escolha == 1:
        print("\nVocê escolheu uma partida!\n")
        partida()
    elif escolha == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()
    else:
        print("\nOpção inválida. Escolha 1 ou 2.")
