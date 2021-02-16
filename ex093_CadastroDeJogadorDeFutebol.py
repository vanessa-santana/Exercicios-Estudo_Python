'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''

cadastro=dict()
golsLista=list()

cadastro['nome']=str(input('Nome do Jogador: ')).strip().title()
partidas=int(input(f'Quantas partidas {cadastro["nome"]} jogou?: '))

for i in range (0,partidas):
    golsLista.append(int(input(f'     Quantos gols na partida {i+1}?: ')))

cadastro['gols']=golsLista[:]
cadastro['total']=sum(golsLista)
print('-='*30)
print(cadastro)
print('-='*30)
for k,v in cadastro.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for i,v in enumerate(cadastro['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols')
print('-='*30)
