#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-”

def crib(a):
    while a != 0:
        if a % 2 == 0 and a % 3 == 0 and a % 5 == 0 and a % 7 == 0 and a % 11 == 0:
            pass
        else:
            print(a)
            a=a-1
    
print("Digites hasta donde decea sacar los numeros primos")
b=(int)(input())
print("los numeros primos son: ")
print(crib(b))