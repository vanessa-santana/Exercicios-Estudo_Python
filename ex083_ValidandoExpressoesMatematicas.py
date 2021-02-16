'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. '''

expr=str(input('Digite a expressão:'))
pilha=[] #toda string é uma lista
for simbolo in expr:
    if simbolo =='(':
        pilha.append('(')
    
    elif simbolo ==')':
        if len(pilha)>0:
            pilha.pop() #remove o ultimo elemento de uma lista
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão esta valida!')
else:
    print('Sua expressão está errada')