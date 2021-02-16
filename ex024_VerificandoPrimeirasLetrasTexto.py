#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".


cidade=str(input('Digite o nome da cidade: ')).strip() #strip() elimina os espaços antes e depois
capitalizado=cidade.title()
print('A cidade {} começa com "Santo"?: {}'.format(cidade,capitalizado[:5]=='Santo'))


