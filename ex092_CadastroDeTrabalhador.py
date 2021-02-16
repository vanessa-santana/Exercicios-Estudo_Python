''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. '''
from datetime import date

cadastro=dict()

cadastro['nome']=str(input('Nome: ')).strip().title()
anoNasci=int(input('Ano de nascimento: '))
idade=(date.today().year)-anoNasci
cadastro['idade']=idade
cadastro['carteiraTrabalho']=int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['carteiraTrabalho'] != 0:
    cadastro['anoContratação']=int(input('Ano de Contratação: '))
    cadastro['salario']=float(input('Salario: R$'))
    cadastro['aposentadoria']=(cadastro['anoContratação']+35)-date.today().year
else: 
    cadastro['carteiraTrabalho']='Sem Registro'


print('-='*30)
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v}')





