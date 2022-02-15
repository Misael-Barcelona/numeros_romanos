#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# PASAR DE NÚMEROS ARÁBIGOS A ROMANOS.

# Declaramos las funciones.

def cuatroCifras(numero):
	cifra = int(numero[0:1])
	respuesta = "M" * cifra
	return respuesta

def tresCifras(cifras, numero):
	if cifras == 4:
		inicio = 1
		fin = 2
	else:
		inicio = 0
		fin = 1
	cifra = numero[inicio:fin]
	if cifra == "1":
		respuesta = "C"
	elif cifra == "2":
		respuesta = "CC"
	elif cifra == "3":
		respuesta = "CCC"
	elif cifra == "4":
		respuesta = "CD"
	elif cifra == "5":
		respuesta = "D"
	elif cifra == "6":
		respuesta = "DC"
	elif cifra == "7":
		respuesta = "DCC"
	elif cifra == "8":
		respuesta = "DCCC"
	elif cifra == "9":
		respuesta = "CM"
	else:
		respuesta = ""
	return respuesta

def dosCifras(cifras, numero):
	if cifras == 4:
		inicio = 2
		fin = 3
	elif cifras == 3:
		inicio = 1
		fin = 2
	else:
		inicio = 0
		fin = 1
	cifra = numero[inicio:fin]
	if cifra == "1":
		respuesta = "X"
	elif cifra == "2":
		respuesta = "XX"
	elif cifra == "3":
		respuesta = "XXX"
	elif cifra == "4":
		respuesta = "XL"
	elif cifra == "5":
		respuesta = "L"
	elif cifra == "6":
		respuesta = "LX"
	elif cifra == "7":
		respuesta = "LXX"
	elif cifra == "8":
		respuesta = "LXXX"
	elif cifra == "9":
		respuesta = "XC"
	else:
		respuesta = ""
	return respuesta

def unaCifra(cifras, numero):
	if cifras == 4:
		inicio = 3
		fin = 4
	elif cifras == 3:
		inicio = 2
		fin = 3
	elif cifras == 2:
		inicio = 1
		fin = 2
	else:
		inicio = 0
		fin = 1
	cifra = numero[inicio:fin]
	if cifra == "1":
		respuesta = "I"
	elif cifra == "2":
		respuesta = "II"
	elif cifra == "3":
		respuesta = "III"
	elif cifra == "4":
		respuesta = "IV"
	elif cifra == "5":
		respuesta = "V"
	elif cifra == "6":
		respuesta = "VI"
	elif cifra == "7":
		respuesta = "VII"
	elif cifra == "8":
		respuesta = "VIII"
	elif cifra == "9":
		respuesta = "IX"
	else:
		respuesta = ""
	return respuesta

# Preguntamos un número y comprobamos que el número introducido esté en el rango correcto.

numero = 0
while numero < 1 or numero > 3999:
	try:
		numero = int(input("Dime un número entre 1 y 3999: "))
	except:
		numero = 0

# Pasamos el número a tipo string.

numero = str(numero)

# Calculamos cuantas cifras tiene.

cifras = len(numero)

# Inicializamos la variable numeroRomano.

numeroRomano = ""

# Iremos calculando el número romano a partir del número facilitado por el usuario.

# Esto se ejecutará si el número tiene 4 cifras.

if cifras == 4:
	numeroRomano = cuatroCifras(numero)

# Esto se ejecutará si el número tiene al menos 3 cifras.

if cifras >= 3:
	numeroRomano += tresCifras(cifras, numero)

# Esto se ejecutará si el número tiene al menos 2 cifras.

if cifras >= 2:
	numeroRomano += dosCifras(cifras, numero)

# Esto se ejecutará si el número tiene al menos 1 cifras.

if cifras >= 1:
	numeroRomano += unaCifra(cifras, numero)

# Muestra el resultado y finaliza el programa.

print(numero + " = " + numeroRomano)
exit(0)
