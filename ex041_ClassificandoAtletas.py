''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER '''

from datetime import date

anoNasc=int(input('Ano Nascimento do Atleta: '))

idade=date.today().year - anoNasc

if idade <= 9:
    print('Idade {}: Mirim'.format(idade))
elif idade <=14:
    print('Idade {}: Infantil'.format(idade))
elif idade <=19:
    print('Idade {}: Junior'.format(idade))
elif idade <=25:
    print('Idade {}: Senior'.format(idade))
else:
    print('Idade {}: Master'.format(idade))


