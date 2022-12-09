from random import randint
pontos_jogador_1 = pontos_jogador_2 = 0
while pontos_jogador_1 < 22 and pontos_jogador_2 < 22:
    if pontos_jogador_1 < 21:
        retirar = str(input('Vez do jogador 1.\nRetirar um número aleatório? [S/N] ')).upper().strip()[0]
        if retirar in 'Ss':
            numero_aleatório = randint(1,10)
            pontos_jogador_1 += numero_aleatório
            print(f'O número sorteado foi {numero_aleatório}.\n\nO jogador 1 agora tem {pontos_jogador_1} pontos!')
        else:
            print('O jogador não retirou nenhum número.')
    else:
        print('O jogador 1 não pode mais jogar!')
    print('-=' * 15)
    if pontos_jogador_2 < 21:
        retirar = str(input('Retirar um número aleatório? [S/N] ')).upper().strip()[0]
        if retirar in 'Ss':
            numero_aleatório = randint(1,10)
            pontos_jogador_2 += numero_aleatório
            print(f'O número sorteado foi {numero_aleatório}.\n\nO jogador 2 agora tem {pontos_jogador_2} pontos!')
        else:
            print('O jogador não retirou nenhum número.')
        print('-=' * 15)
    else:
        print('O jogador 2 não pode mais jogar!')
print(f'\nO jogador 1 tem {pontos_jogador_1} pontos e o jogador 2 tem {pontos_jogador_2} pontos!')

''' Regras:
O jogador que tiver pontos mais próximo de 21 ou exatamente vence.
Se o jogador passar de 21 pontos perde automáticamente.
v2.0
'''
