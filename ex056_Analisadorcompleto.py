''' Desenvolva um programa que leia o 
    nome, 
    idade e 
    sexo de 4 pessoas.
No final do programa, mostre: 
a média de idade do grupo,
 qual é o nome do homem mais velho e 
 quantas mulheres têm menos de 20 anos. '''

media=0
somaIdad=0
nomeMasc=''
contTotal=0
contIdMasc=0
IdFem=0
contIdFem=0

for i in range (1,5):
    print('------------ {}ª Pessoa ------------.'.format(i))
    nome=str(input('Digite o nome: '))
    idade=int(input('Digite a idade: '))
    sexo=str(input('Digite o sexo:(F) ou (M) ')).upper()

    contTotal+=1
    somaIdad+=idade

    if i==1 and sexo == 'M':  #se não usar o upper acima: " and sexo in 'Mm' "
        contIdMasc=idade
        nomeMasc=nome
       
    if sexo== 'M' and idade >contIdMasc:
        contIdMasc=idade
        nomeMasc=nome
    
    if sexo=='F' and idade < 20:
        contIdFem+=1
     
media = somaIdad/contTotal
    
print('media da idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(contIdMasc,nomeMasc))
print('A quantidade de mulheres que tem menos de 20 anos é {}'.format(contIdFem))

