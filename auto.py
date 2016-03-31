class auto(object):
    def __init__(self, kilometraje, bencina, rendimiento):
        self.kilometraje = kilometraje
        self.bencina = bencina
        self.rendimiento   = rendimiento
        self.arrancado=False
        self.velocidad=0
        
    def acelerar(self):
         if self.arrancado :
            self.velocidad = self.velocidad + 1
            if self.velocidad -1  == self.kilometraje:
                self.velocidad= self.kilometraje
                    
            return self.velocidad
      
    def obtenerKilometraje (self):
         return self.cuenta_kilometros
     
    def encender(self):
        if self.arrancado== False:
            print('Roarrrr')
            self.arrancado = True
        else:
            # Dale al encendido estando el coche arrancado y escucha...
            print('kggggg')
               
    def apagar(self):
                print("llegando a la bencinera apagar auto")
                self.arrancado = False
               
    def encendido(self):
                self.arrancado= True   
                   
    def obtenerBencina(self):
                return self.bencina
               
    def cargarBencina(self):
                if self.arrancado == False:
                    print("cargando bencina")
                    print("bencina cargada")
                else:
                    print("apaga motor")
    
if __name__ == "__main__":
               
               kil=int(input("ingrese kilometraje del vehiculo: "))
               benci=int(input("Ingrese bencina: "))
               rend=float(input("Rendimiento(k/L): "))                                   
               autonuevo=auto(kil,benci,rend)
               autonuevo.encender()
               while(autonuevo.bencina != 0 ):
                   autonuevo.acelerar()
                   if(autonuevo.velocidad==kil):
                     autonuevo.bencina=autonuevo.bencina -1                      
                  
               if (autonuevo.bencina==0):
                   autonuevo.apagar()
                   autonuevo.cargarBencina()
               autonuevo.encendido()
               print("Chao bencinera ")
