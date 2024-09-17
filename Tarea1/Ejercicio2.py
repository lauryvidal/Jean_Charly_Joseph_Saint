#Operaciones Matemáticas en un Proyecto
#Escribe un programa que pida al usuario ingresar su peso en kilogramos y su altura en metros.
#Calcula el IMC utilizando la fórmula mencionada.
#Muestra el IMC del usuario con un mensaje que diga: "Tu IMC es [IMC]."

peso = float(input(f"Ingrese su peso en kilogramos:"))
altura = float (input(f"Ingrese su altura en metro:"))

imc = peso / (altura**2)

print (f"Tu IMC es {imc}.")