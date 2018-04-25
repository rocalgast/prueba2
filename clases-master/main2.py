class Cliente:
    def __init__(self):
        self.nombre=""
        self.direccion=""
        self.telf=0
        self.email=""

        self.cotizacion=0


    def mostrar(self):
        print (self.nombre, self.direccion)
    def setCotizacion(self,cotizacion):
        self.cotizacion=cotizacion

indra=Cliente()

indra.setCotizacion(300)

print(indra.cotizacion)
pepe=Cliente()
pepe.nombre="pepe"
print (pepe.nombre)
pepe.direccion="vitoria"
print (pepe.direccion)
pepe.telf=945
print (pepe.telf)
pepe.email="gmail"
print (pepe.email)

pepe.mostrar()

print (pepe)


class Cliente:
    def __int__(self):

