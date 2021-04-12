# importando bibliotecas necessarias
from turtle import Turtle
from time import time

# incializando a turtle
t = Turtle()
# definir a velocidade
t.speed(1)
# comandos
desenho = 1
while True:
    if desenho == 1:
        opcao = int(input('Quer desenhar?\n1 - Sim\n2 - Não\nResposta: '))
    else:
        opcao = int(input('\nQuer continuar?\n1 - Sim\n2 - Não\nResposta: '))

    if opcao == 1:
        andar = int(input(
            '\nPara qual posição a tartaruga deve ir?\n1 - para frente\n2 - para trás\nResposta: '))
        if andar == 1:
            pixels = int(
                input('\nQuantos pixels você deseja andar?\nResposta:  '))
            grau = int(input(
                '\nDeseja rotacionar o cursor?\n1 - para direita\n2 - para esquerda\n3 - não rotacionar\nResposta: '))
            if grau == 1:
                graus = int(
                    input('\nQuantos graus quer rotacionar?\nResposta: '))
                t.right(graus)
                t.forward(pixels)
            elif grau == 2:
                graus = int(
                    input('\nQuantos graus quer rotacionar?\nResposta: '))
                t.left(graus)
                t.forward(pixels)
            else:
                t.forward(pixels)

        elif andar == 2:
            pixels = int(
                input('\nQuantos pixels você deseja andar?\nResposta: '))
            grau = int(input(
                '\nDeseja rotacionar o cursor?\n1 - para frente\n2 - para trás\n3 - não rotacionar\nResposta: '))
            if grau == 1:
                graus = int(
                    input('\nuQuantos graus quer rotacionar?\nResposta: '))
                t.right(graus)
                t.back(pixels)
            if grau == 2:
                graus = int(
                    input('\nQuantos graus quer rotacionar?\nResposta: '))
                t.left(graus)
                t.backward(pixels)
            else:
                t.backward(pixels)
        else:
            opcao = ''
            print('\n COAMNDO INVALIDO')

        desenho += 1
    else:
        break
