#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-”
def mcd(a, b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)

def mcd2(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a

print("Introduce el primer numero: ")
num1 = (int)(input())
print("Introduce el segundo numero: ")
num2 = (int)(input())
#a = (int)(mcd(num1, num2))
#b=(int)(mcd2(num1,num2))

print("El MCD normal de " + str(num1), " y ", str(num2), " es: ", str(mcd(num1,num2)))
print("El MCD de recursivo " + str(num1), " y ", str(num2), " es: ", str(mcd2(num1,num2)))
