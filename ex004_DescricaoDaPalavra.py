#Faça um programa que leia algo pelo tclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

var=input('Digite algo:')
print('O tipo primitivo deste valor é: ', type(var))
print('Só tem espaços? ', var.isspace())
print('É um número? ', var.isnumeric())
print('É alfabético? ', var.isalpha())
print('É alfabumérico? ', var.isalnum())
print('Esta em maiusculo? ', var.isupper())
print('Esta em minusculo? ', var.islower())
print('Esta capitalizado? ', var.istitle())
