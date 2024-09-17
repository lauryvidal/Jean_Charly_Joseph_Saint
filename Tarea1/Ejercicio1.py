#Registro de Usuario
#Escribe un programa que pida al usuario ingresar su nombre, apellido, edad y altura.
#Almacena esta información en variables.
#Muestra la información del usuario en una oración que diga: "El usuario [Nombre] [Apellido] tiene [Edad] años y una altura de [Altura] metros."

nombre = input(f" Ingrese tu nombre:")
apellido = input(f" Ingrese tu apellido:")
edad = int(input(f" Ingrese tu edad:"))
altura = float(input(f" Ingrese tu altura:"))
print (f"El usuario {nombre} {apellido} tiene {edad} años y una altura de {altura} metros.")