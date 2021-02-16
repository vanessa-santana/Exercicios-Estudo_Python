#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('cateto oposto:' ))
ca = float(input('cateto adjacente:' ))
hi=hypot(co,ca)
print('hipoentusa é {:.2f}'.format(hi))