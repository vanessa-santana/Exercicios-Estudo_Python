'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense. '''

times=('Corinthians','Palmeiras','Santos','Gremio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atletico','Botafogo',
'Atletico-PR','Bahia','Sao Paulo','Fluminense','Sport-Recife','EC Vitoria','Coritiba','Avai','Ponte Rasa','Atletico-GO')

print('-='*15)
print(f'Lista de Times: {times}')
print('-='*15)
#for t in times:
#    print(t)

print(f'Os cincos primeiros são: {times[0:5]}')
print('-='*15)

print(f'Os quatros ultimos são: {times[-4:]}')
print('-='*15)

print(f'Times em ordem alfabetica são : {sorted(times)}')
print('-='*15)

print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição')