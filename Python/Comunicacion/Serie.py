import serial
import time

def main():
    puerto_serie = serial.Serial()
    puerto_serie.port = "/dev/ttyUSB0"
    puerto_serie.baudrate = 9600
    puerto_serie.parity = serial.PARITY_NONE
    #puerto_serie.timeout = 1
    puerto_serie.stopbits = serial.STOPBITS_ONE
    puerto_serie.bytesize = serial.EIGHTBITS
    
    cadena = bytearray(1)
    # Aqui se abre el puerto serie
    puerto_serie.open()

    cadena[0]= 62
    time.sleep(1)
    if puerto_serie.is_open:
        puerto_serie.write(cadena)
        time.sleep(0.01)
        res = puerto_serie.read(1)
        print(res, 
              int.from_bytes(res), 
              res.decode(), 
              ' '.join('{0:02X}'.format(e) for e in res))
    puerto_serie.close()






if __name__=="__main__":
    main()