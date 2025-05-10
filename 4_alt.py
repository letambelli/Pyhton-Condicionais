x = int(input('x: '))
y = int(input('y: '))

match (x, y):
    case (0, 0):
        print('O ponto está na origem.')
    case (_, 0):
        print('O ponto está sobre o eixo x.')
    case (0, _):
        print('O ponto está sobre o eixo y.')
    case (x, y) if x > 0 and y > 0:
        print('Primeiro Quadrante.')
    case (x, y) if x < 0 and y > 0:
        print('Segundo Quadrante.')
    case (x, y) if x < 0 and y < 0:
        print('Terceiro Quadrante.')
    case (x, y) if x > 0 and y < 0:
        print('Quarto Quadrante.')
