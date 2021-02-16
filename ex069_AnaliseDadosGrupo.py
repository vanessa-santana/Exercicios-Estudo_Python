''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

mais18 = qtdHomens = qtdMulheresJovens=0
while True:
    print('----- Cadastro De Pessoas -----')
    idade=int(input('Digite a idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    print('-'*30)
    if idade > 18 :
        mais18+=1
    if sexo in 'Mm':
        qtdHomens+=1
    if idade < 20 and sexo=='F':
        qtdMulheresJovens+=1

    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N]: ')).strip()[0].upper()
    if resp =='N':
        break

print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {qtdHomens} homens cadastrados')
print(f'E temos {qtdMulheresJovens} mulheres com menos de 20 anos')

