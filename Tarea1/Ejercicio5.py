#Cálculo de Promedio de Notas
#Escribe un programa que permita al usuario ingresar una serie de notas.
#Calcula el promedio de las notas ingresadas.
#Muestra el promedio con un mensaje que diga: "El promedio de tus notas es [Promedio]."

insertado = input(f"Inserta una nota, semarado con coma:")

notas = insertado.split(',')

notas= [float (nota) for nota in notas]

promedio1 = sum(notas) / len (notas)

print (f"El promedio de tus nota es {promedio1}")