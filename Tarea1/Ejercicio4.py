#Listas de Compras
#Escribe un programa que permita al usuario agregar ítems a una lista de compras hasta que decida dejar de agregar más ítems.
#Una vez que el usuario decida detenerse, muestra todos los ítems que han sido agregados a la lista.

listaDeCompra = []
listado = True

while (listado):
    print("inserte en la lista, escribe detenerse si quiere terminar:")
    lista = input()

    if lista == "Detenerse" or lista == "detenerse":
        listado = False
        break
    else:
        listaDeCompra.append(lista)

print (f"Tu lista tiene: {listaDeCompra}")