listita=[]
lista = raw_input("Ingresa frase: ")
while (lista!=" "  ):
    listita += [lista] 
    lista = raw_input("Ingresa frase: ")
    
print ("las frases ingresadas fueron: ")
print listita
nueva_lista=' '.join(listita)
print nueva_lista.upper()



