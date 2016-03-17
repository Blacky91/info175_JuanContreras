def funcion(x,y):
    if x < y:
        print("el numero menor es", x)
        print("el numero mayor es ", y)
    elif y< x:
        print("el numero menor es", y)
        print("el numero mayor es", x)
    elif x==y :
        print("Ambos numeros son iguales")

    
if __name__== "__main__":
        x=input("ingrese un numero entero: ")
        y=input("ingrse numero entero: ")
        funcion(x,y)
        print("chao")
