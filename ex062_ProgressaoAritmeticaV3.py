''' Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos. '''

print('Gerador de PA')
print('-='*15)
primeiroTermo=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))

ultimotermo=primeiroTermo + (10-1)*razao
contador=0

for i in range (primeiroTermo,ultimotermo+razao,razao):
    print('{} -> '.format(i),end='')
    contador+=1
print('PAUSA')

sair=False
while not sair:
    maistermo=int(input('Quantos termos você quer mostrar a mais: '))
    if maistermo!=0:
        primeiroTermo=i+razao
        ultimotermo=primeiroTermo +(maistermo-1)*razao
        for i in range (primeiroTermo,ultimotermo+razao,razao):
            print('{} -> '.format(i),end='')
            contador+=1
        print('PAUSA')
    else:
        sair=True
        print('Progressao Finalizada com {} termos'.format(contador))

'''outro modo

print('Gerador de PA')
print('-='*15)
primeiro=int(input('Digite o primeiro termo: '))
razao=int(input('Digite a razao: '))
termo=primeiro
cont=1
total=0
mais=10

while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo),end='')
        termo +=razao
        cont +=1
    print('PAUSA')
    mais=int(input('Quantos termos a mais: '))
print('Progressao finalizada com {} termos'.format())