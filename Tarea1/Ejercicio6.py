#Ejercicio6
#Escribe un programa que convierta una temperatura de Celsius a Fahrenheit.
#Escribe un programa que convierta una temperatura de Fahrenheit a Celsius.
#Utilize este programa para convertir una temperatura dada en ambas direcciones y muestra los resultados.

celsius = float(input(f"Inserta temperatura de Celsius:"))
fahrenheit  = ((celsius*9)/5)+32
print(f"Esta temperatura en Fahrenheit es {fahrenheit}")

fahrenheit = float(input(f"Inserta temperatura de Fahrenheit:"))
celsius  = ((fahrenheit-32)*5)/9
print(f"Esta temperatura en Celsius es {celsius}")