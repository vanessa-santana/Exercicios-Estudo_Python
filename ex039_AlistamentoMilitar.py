'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
 do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

anoNasc=int(input('Digit o ano de nascimento: '))

idade=date.today().year-anoNasc
print('Ano de nascimento: {}'.format(anoNasc))
print('Quem nasceu em {} tem {} em {}'.format(anoNasc,idade,date.today().year))
if idade < 18:
    dif=18-idade
    print('E faltam {} anos para se alistar.'.format(dif))
elif idade > 18:
    dif=idade-18
    print('Passaram {} anos do alistamento.'.format(dif))
else:
 print('Tem que se alistar imediatamente!')