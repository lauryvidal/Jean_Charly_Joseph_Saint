#Evaluación de Edad
#Escribe un programa que pida al usuario ingresar su edad.
#Utiliza una estructura condicional para determinar si la persona es un adulto (18 años o más) o un menor (menos de 18 años).
#Muestra un mensaje que diga: "Eres adulto" o "Eres menor", según corresponda.

edad= int(input(f"Ingresa tu edad:"))

if (edad >= 18):
    print (f"Eres adulto.")
elif (edad < 18):
    print (f"Eres meno.")