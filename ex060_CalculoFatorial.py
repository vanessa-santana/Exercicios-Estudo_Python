
from math import factorial

number=int(input('digite o numero: '))
fator=factorial(number)

print('O fatorial de {} é {}.'format(number,fator))

#Outro modo
print('Calculando {}! = '.format(number), end='')
contador=number
fatorial=1 #em multiplicação sempre inicializar com 1 . E soma com 0
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador >1 else ' = ', end='')
    fatorial*=contador
    contador-=1
print('{}.'format(fatorial))

