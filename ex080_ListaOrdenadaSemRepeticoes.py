#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

listaNum=[]

for contador in range(0,5):
    num=int(input('Digite um valor: '))

    if contador==0 or num > listaNum[-1]: #OU listaNum[len(listaNum)-1]:
        listaNum.append(num)
        print('Adicionado ao final da lista...')
    else:
        posicao=0
        while posicao < len(listaNum):
            if  num <= listaNum[posicao]:
                print(listaNum[posicao])
                listaNum.insert(posicao,num)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao+=1
        

print('-='*30)
print(listaNum)
