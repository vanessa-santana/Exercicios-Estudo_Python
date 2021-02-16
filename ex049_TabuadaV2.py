#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.


num=int(input('Digite um numero inteiro: '))
print('-'*12)
for n in range (0,11):
    print('{:2}  x {:2} = {:2}'.format(n,num,n*num))

print('-'*12)