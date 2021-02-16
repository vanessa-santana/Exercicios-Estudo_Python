'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
  de cada aluno individualmente. '''

ficha=list()
nota1=nota2=media=0

while True:
    nome=str(input('Digite o nome: ')).title()
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])

    resp=' '
    while resp not in 'SN':
        resp=str(input('Deseja continuar?: ')).strip()[0].upper()

    if resp == 'N':
        break

print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"Média":>8}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-='*35)
    opcao=int(input('Mostrar notas de qual aluno? (999 intemrromper): '))

    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha)-1: 
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')

print('<<< VOLTE SEMPRE >>>')


