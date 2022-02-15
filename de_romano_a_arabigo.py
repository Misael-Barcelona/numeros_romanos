#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# PASAR DE NÚMEROS ROMANOS A ARÁBIGOS.

# Definimos las tuplas.

romanos = ("I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M")
arabigos = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)

# Preguntamos un número romano y lo guardamos en la variable numero en mayúsculas.

numero = input("Dime un número romano: ").upper()

# Comprobamos que el número facilitado sea correcto.

# Comprobación por letras.
# Se comprueba si las letras introducidas son números romanos.
# La variable esRomano será True si encuentra la letra en la tupla correspondiente.

# Inicializamos la variable esRomano como False.

esRomano = False

# Con el primer for vamos pasando por cada una de las letras del número romano que nos ha pasado el usuario.

for letra in numero:

	# En el segundo for comprobamos si la letra es un número romano buscándola en la tupla correspondiente.

	for indice in range(len(romanos)):

		# En el momento que encuentra la letra en la tupla asigna el valor True a la variable esRomano y sale del seguno for.
	
		if letra == romanos[indice]:
			esRomano = True
			break

	# Al salir del segundo for comprueba el valor de esRomano.
	# Si es False querrá decir que una de las letras introducidas no es un número romano y el programa terminará.
	# Si es True querrá decir que la letra introducida es un número romano y pasaremos a comprobar la siguiente letra.

	if esRomano == False:
		print("El número romano introducido es incorrecto.")
		exit(0)
	else:
		esRomano = False

# Si llegamos a este punto quiere decir que todas las letras que componen el número romano son correctas.
# Pero tal vez el formato no sea del todo correcto. Tenemos que comprobarlo.

# Primero comprobamos que no haya más repeticiones de las permitidas.

if numero.find("IIII") != -1 or numero.find("XXXX") != -1 or numero.find("CCCC") != -1 or numero.find("MMMM") != -1 or numero.find("VV") != -1 or numero.find("LL") != -1 or numero.find("DD") != -1:
 	print("El número romano introducido es incorrecto.")
 	exit(0)

# También comprobaremos convinaciones incorrectas.

if numero.find("IIV") != -1 or numero.find("IIX") != -1 or numero.find("XXL") != -1 or numero.find("XXC") != -1 or numero.find("CCD") != -1 or numero.find("CCM") != -1:
  	print("El número romano introducido es incorrecto.")
  	exit(0)

# Procedemos a hacer la conversión de romano a arábigo.
# En primer lugar, comprobaremos si el número introducido consta de 1, 2 o más caracteres.  

# Inicializamos la variable numeroArabigo.

numeroArabigo = 0

# En caso de que el número romano tenga sólo un carácter se ejecutará esto:

if len(numero) == 1:
	for letra in numero:
		for indice in range(len(romanos)):
			if letra == romanos[indice]:
				numeroArabigo = arabigos[indice]
				break	

# En caso de que el número romano tenga dos caracteres se ejecutará esto:

elif len(numero) == 2:
	for indice in range(len(romanos)):
		if numero == romanos[indice]:
			numeroArabigo = arabigos[indice]
			break

	if numeroArabigo == 0:
		for letra in numero:
			for indice in range(len(romanos)):
				if letra == romanos[indice]:
					numeroArabigo += arabigos[indice]
					break

# En caso de que el número romano tenga más de dos caracteres se ejecutará esto:

else:
	numeroAnterior = numeroArabigo
	posicionInicial = 0 
	while posicionInicial < len(numero):
		letra = numero[posicionInicial:posicionInicial+2]
		for indice in range(len(romanos)):
			if letra == romanos[indice]:
				numeroArabigo += arabigos[indice]
				posicionInicial += 2
				break

		if numeroArabigo == numeroAnterior:
			letra = numero[posicionInicial:posicionInicial+1]
			for indice in range(len(romanos)):
				if letra == romanos[indice]:
					numeroArabigo += arabigos[indice]
					posicionInicial += 1
					break

		numeroAnterior = numeroArabigo
		
# Finalmente se muestra el resultado y finaliza el programa. 

print(numero + " = " + str(numeroArabigo))
exit(0)
