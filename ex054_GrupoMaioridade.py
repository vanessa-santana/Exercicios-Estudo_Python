
#Crie um programa que leia o ano de nascimento de sete pessoas.
#  No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual=date.today().year
contMaiores=0
contMenores=0
for i in range (1,7,1):
    anoNasc=int(input('Em que ano a {}ª pessoa masceu?: '.format(i)))
    idadeAtual=atual - anoNasc
    if idadeAtual <18:
        contMenores+=1
    else:
        contMaiores+=1
    print('Tem {} anos'.format(idadeAtual,end=''))

print('\nPossui {} maiores de idade e {} menores de idade'.format(contMaiores,contMenores))
    
