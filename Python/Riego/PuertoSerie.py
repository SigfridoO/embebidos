import serial
import time

from Convertidor import Convertidor

class PuertoSerie:
    def __init__(self):
        self.puerto_serie = serial.Serial()
        self.puerto_serie.port = "/dev/ttyUSB0"
        self.puerto_serie.baudrate = 115200
        self.puerto_serie.parity = serial.PARITY_NONE
        self.puerto_serie.timeout = 1
        self.puerto_serie.stopbits = serial.STOPBITS_ONE
        self.puerto_serie.bytesize = serial.EIGHTBITS

    def abrir(self):
        self.puerto_serie.open()

    def enviar_mensaje (self, mensaje):
        res = None
        if self.puerto_serie.is_open:
            self.puerto_serie.write(mensaje)
            time.sleep(0.01)
            res = self.puerto_serie.read(25)
            print("Respuesta >>: ", res) 
                #  " >> "
                #   ' '.join('{0:02X}'.format(e) for e in res))
        return res
    def cerrar(self):
        self.puerto_serie.close()

def main():
    puerto_serie = PuertoSerie()

if __name__=="__main__":
    main()