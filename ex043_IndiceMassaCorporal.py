''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida '''

peso=float(input('Peso: '))
alt=float(input('Altura: '))

imc=peso/(alt**2)

if imc < 18.5:
    print('Altura {}, peso {} = IMC {:.2f} : Abaixo do peso'.format(alt,peso,imc))
elif 18.5 <= imc < 25:
    print('Altura {}, peso {} = IMC {:.2f} : Peso Ideal'.format(alt,peso,imc))
elif 25 <= imc <30:
    print('Altura {}, peso {} = IMC {:.2f} : Sobrepeso'.format(alt,peso,imc))
elif 30 <= imc <40:
    print('Altura {}, peso {} = IMC {:.2f} : Obesidade'.format(alt,peso,imc))
else:
    print('Altura {}, peso {} = IMC {:.2f} : Obesidade morbida'.format(alt,peso,imc))
    
