class auto():
    pass

class Acoplado():

    cantidad_acoplados = 0

    def __init__(self, ruedas=8, peso = 1000, carga = "vacio"):
        self.ruedas = ruedas
        self.peso = peso
        self.carga = carga
        Acoplado.cantidad_acoplados += 1
        
    
class Camion(auto):

    cantidad = 0
    
    def __init__(self, peso_camion= 5.8, ruedas_camion = 6,):
        self.peso = float(peso_camion)
        self.ruedas = int(ruedas_camion)
        Camion.cantidad +=1
        self.acoplados = list()
        
    def agregar_acoplado(self, ruedas, peso, carga):
        self.acoplados.append(
            Acoplado(ruedas=ruedas, peso= peso, carga=carga))

    def quitar_acoplado(self,acop):
        self.acoplados.pop()

    def obtener_acoplados(self):
        print("sus acoplados son: " ,self.acoplados)

    def obtener_ruedas(self):
        total = self.ruedas # las ruedas del camion
        for a in self.acoplados:
            total += a.ruedas
        return total

    def obtener_peso(self):
        return self.peso + sum([x.peso for x in self.acoplados])


if __name__ == "__main__":
    a = Camion()
    b = Camion(peso = 6000, ruedas = 6)
    c = Camion(3000, 4)    

    a.agregar_acoplado(4,1000,"cerveza")
    print(a.obtener_ruedas())
    print(a.obtener_peso())
