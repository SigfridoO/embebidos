import serial
import time

from Convertidor import Convertidor

def main():
    puerto_serie = serial.Serial()
    puerto_serie.port = "/dev/ttyUSB0"
    puerto_serie.baudrate = 9600
    puerto_serie.parity = serial.PARITY_NONE
    puerto_serie.timeout = 1
    puerto_serie.stopbits = serial.STOPBITS_ONE
    puerto_serie.bytesize = serial.EIGHTBITS
    
    #cadena = bytearray(1)
    # Aqui se abre el puerto serie
    puerto_serie.open()

    convertidor = Convertidor()
    mensaje = convertidor.generar_mensaje(0, 0)
    print("El mensaje es: ", mensaje)
    time.sleep(1)
    if puerto_serie.is_open:
        puerto_serie.write(mensaje)
        time.sleep(0.01)
        res = puerto_serie.read(25)
        print("Respuesta >>: ", res) 
            #  " >> "
            #   ' '.join('{0:02X}'.format(e) for e in res))
    puerto_serie.close()

if __name__=="__main__":
    main()