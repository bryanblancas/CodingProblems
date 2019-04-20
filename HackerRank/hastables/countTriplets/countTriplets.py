#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys
from math import factorial

# Complete the countTriplets function below.
def countTriplets(arr, r):

	####Implementar defaultdic para evitar la validación de si existe un número en la hashtable

	#Los números iniciales no nos importan, sólo toma relevancia poder decir cuando se encontro un 3er número de la tripleta o un segundo número para poder encontrar su tercero

	ht = {} #Llevar un control de los 2do números <number_key , número_repeticiones>
	ht2 = {} #Llevar un control de los 3eros números <number_key , número_tripletas_generadas>
	triplets = 0

	if r == 1:
		number_ones = 0
		for number in arr:
			if number == 1:
				number_ones += 1
		
		return factorial(number_ones) // (factorial(3) * factorial(number_ones - 3))

	#Recorremos el arreglo elemento por elemento
	for number in arr:

		#Si el número es un 2do número de una tripleta, entonces ya sólo necesitamos su 3er número de la tripleta. Al 3er número de la tripleta le sumamos las veces que se repite su 2do número, porque es el número de tripletas que se han generado gracias a este número
		if number in ht:
			if number*r in ht2:
				ht2[number*r] += ht[number]
				print(ht2)
			else:
				ht2[number*r] = ht[number]
				print(ht2)

		#Si el número es un 3er número de una tripleta, entonces hemos encontrado una tripleta y actualizamos el contador de tripletas
		if number in ht2:
			triplets += ht2[number]
			#print(ht2)
			
		#Agregamos nuestro número actual por r (number*r) al ht, es decir, agregamos un nuevo posible 2do número de una tripleta, el cual estaremos buscando posteriormente. Se suma su valor anterior porque actualizamos su contador para saber cuantas veces lo tenemos 
		if number*r in ht:
			ht[number*r] += 1
		else:
			ht[number*r] = 1

		print("------------")

	return triplets

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    file = open("countTriplets.txt", 'r')
    nr = file.readline().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, file.readline().rstrip().split()))

    #r = 1
    #arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
	#    		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    #		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    #		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    #		1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    

    ans = countTriplets(arr, r)

    print ans
    #fptr.write(str(ans) + '\n')

    #fptr.close()
