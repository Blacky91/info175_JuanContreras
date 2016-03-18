def ordena():
    lista = []
    lista = x.split(",")
    print "Lo que usted ingreso"
    print (lista)
    lista.sort()
    print "Acabamos de ordenar lo ingresado"
    print(lista)


if __name__ == "__main__":
	x = raw_input("ingrese palabras separadas con comas:  ")	
	ordena()
        
