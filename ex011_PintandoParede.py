#Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura=float(input('Digite a medida da largura: '))
altura=float(input('Digite a medida da altura: '))

area=largura*altura
litroTinta = (area/2)

print('Para a altura de {} e largura de {} possui area de {}. E para esta area são necessarios {:.1f} litros de tinta'.format(altura,largura,area,litroTinta))