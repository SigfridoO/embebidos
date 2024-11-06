from struct import pack, unpack

class Convertidor:
    def __init__(self):
        self.cadena = bytearray(25)
        self.indice = 0
        self.comprobacion = 0

    def generar_mensaje(self,tipo_instruccion, num_instruccion, args = []):
        print("los argumentos son: ", args)
        self.indice = 0
        self.comprobacion = 0
        self.agregar_caracteres("*RIE")
        self.agregar_entero1(tipo_instruccion)
        self.agregar_entero1(num_instruccion)



        self.agregar_entero1(self.indice)
        self.agregar_entero1(self.comprobacion)
        self.agregar_caracteres("?")
        return self.cadena[0:self.indice]
    
    def agregar_entero1(self, numero:int):
        arreglo = pack('B', numero)
        self.agregar_bytes(arreglo)

    def agregar_caracteres(self,texto:str):
        arreglo= texto.encode('ascii')
        self.agregar_bytes(arreglo)

    def agregar_bytes(self, arreglo:bytes):
        for i, elemento in enumerate(arreglo):
            self.cadena[self.indice] = arreglo[i]
            self.indice =self.indice +1
            self.comprobacion ^= arreglo[i]

def main():
    convertidor = Convertidor()
    mensaje = convertidor.generar_mensaje(0, 12)
    print ("El mensaje es: ", mensaje)
    print ([f"{l:02X}"for l in mensaje])

    # numero = 127
    # arreglo = pack('h', numero)
    
    # #print(b'*')
    # print('hola'.encode('ascii'))

if __name__ == "__main__":
    main()