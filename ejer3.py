def funcionmayus():

    print ("las frases ingresadas fueron: ")
    print listamin
    nueva_lista=' '.join(listamin)
    print nueva_lista.upper()

if __name__== "__main__":
    
    lista = raw_input("Ingresa frase: ")
    listamin=[]
    while (lista!=" "):
        listamin += [lista] 
        lista = raw_input("Ingresa frase: ")
    funcionmayus()
    

