def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    lista=[]   
    size=int(input("ingrese el tamaño: "))
    for i in range (size):
        if multiple(i,3) and multiple (i,7):
            lista.append(i)
    print(lista)
    input("presione enter para finalizar")
    
