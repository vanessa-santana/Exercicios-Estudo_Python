#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario=(float(input('Digite o salario: R$ ')))
novoSal= salario*1.15
#ou
#novoSal= salario+(salario*15/100)

print('O valor do salario é de R$ {:.2f} com 15% de aumento ficará R$ {:.2f}'.format(salario,novoSal) )