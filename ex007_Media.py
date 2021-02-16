#Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre a sua média

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))

print('As notas foram {:.1f} e {:.1f}, e a média é: {:.1f}'.format(nota1,nota2,((nota1+nota2)/2)))