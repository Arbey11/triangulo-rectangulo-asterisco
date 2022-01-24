'''Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo, de altura el número introducido'''

from re import I


num = int(input('Ingrese numero: '))

for i in range (num):
    for j in range (i+1):
        print('*',end=' ')
    print()