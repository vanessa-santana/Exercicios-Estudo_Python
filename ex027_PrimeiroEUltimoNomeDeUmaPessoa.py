#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name=str(input('Digite o nome completo: ')).strip()

nameLista=name.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nameLista[0]))
print('Seu último nome é {}'.format(nameLista[len(nameLista)-1]))
