#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario=float(input('Digite o salario R$ '))

if salario <= 1250:
    newSalario=(salario*1.15)
else:
    newSalario=(salario*1.1)
print('Quem ganhava R${:.2f} passará a receber R${:.2f}'.format(salario,newSalario))