''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. '''

extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    number=int(input('Digite um numero entre 0 e 10: '))
    if 0<= number <=10:
        break
    print('Tente novamente. ', end=' ')
   
print(f'Digitou o numero {extenso[number]}')