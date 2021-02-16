#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
#  mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))

termo=primeiroTermo
contador=1
while contador <=10:
    print('{} -> '.format(termo),end='')
    termo=termo+razao
    contador+=1
print('Fim')


