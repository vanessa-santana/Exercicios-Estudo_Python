#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
#setar as variaveis
soma=0
cont=0

#laço (numeros impares de 1 a 500)
for num in range (1,501,2):
    #verificação de multiplos de 3
    if num %3==0:
        print(num, end=' ') #imprime os numeros
        cont=cont+1 #contador
        soma=soma+num #soma

print('\nA soma dos numeros multiplos de 3 é: {}'.format(soma))
print('Quantidade de numeros multiplos de 3 é: {}'.format(cont))