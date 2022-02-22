from math import sqrt
print('Olá Mundo!')


def baskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    print(f'delta = {delta}')
    xv = -b / (2 * a)
    yv = -delta / (4 * a)
    print(f'xv = {xv}')
    print(f'yv = {yv}')
    if (delta > 0):
        x1 = (b - sqrt(delta)) / (2 * a)
        x2 = (b + sqrt(delta)) / (2 * a)
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
    elif(delta == 0):
        print(f'x1 = x2 = {xv}')
    else:
        if (xv == 0):
            x1 = -sqrt(-delta) / (2 * a)
            x2 = sqrt(-delta) / (2 * a)
            print(f'x1 = {x2}i')
            print(f'x2 = {x1}i') 
        else:
            img = sqrt(-delta) / (2 * a)
            print(f'x1 = {xv} + {img}i')
            print(f'x2 = {xv} - {img}i')
            
                     
baskara(1, 0, 36)    
