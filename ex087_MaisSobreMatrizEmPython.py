''' Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. '''

matriz=[[0,0,0],[0,0,0],[0,0,0]]
somaPares=maior=somaColuna=0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para ({linha},{coluna}): '))

print('-='*30)
print('A matriz: ')
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'{matriz[linha][coluna]:^5}',end='')
        if matriz[linha][coluna]%2==0:
            somaPares+=matriz[linha][coluna] 

    print()
print('-='*30)
print(f'A) A soma de todos os valores pares é: {somaPares}')

for linha in range (0,3):
    somaColuna+=matriz[linha][2]
print(f'B) A soma dos valores da terceira coluna é: {somaColuna}')

for coluna in range (0,3):
    if coluna==0:
        maior=matriz[1][coluna]
    elif matriz[1][coluna]>maior:
        maior=matriz[1][coluna]
print(f'C) O maior valor da segunda linha é: {maior}')
