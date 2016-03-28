import string

def Cifrar_Cesar(palabra, salto=2):
        abcd = string.ascii_lowercase
        encrypt_word = ""
        for char in palabra:
            if char != " ":
                index = (abcd.index(char.lower())+salto) % len(abcd)
                encrypt_word +=abcd[index]
            else:
                encrypt_word += char
        return encrypt_word

if __name__== "__main__":
    palabra = raw_input("ingrese pasalabra a incriptar: ")
    print(Cifrar_Cesar(palabra, 3))
