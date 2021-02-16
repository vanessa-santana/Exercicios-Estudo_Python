# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

primTermo=int(input('Digite o primeiro termo inteiro: '))
razao=int(input('Digite a razao: '))

decimoTermo= primTermo+(10-1)*razao

for i in range(primTermo,decimoTermo+razao,razao):
    print(i,end=' -> ')

print('ACABOU')