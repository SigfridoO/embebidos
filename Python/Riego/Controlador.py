import time 
import threading

from PuertoSerie import PuertoSerie
from Convertidor import Convertidor

ADMINISTRACION = '0'


CONTROL = 49
MOD_BANDERA = 52

class Controlador:
    def __init__(self, nombre: str=""):
        super().__init__()
        print('Dentro del constructor de controlador')

        self.led_real =False
        self.led = False
        self.nombre = nombre
        self.funcionando = False
        self.tarea = threading.Thread(target=self.run_controlador)

        self.worker = None

        self.contador = 0
        self.convertidor = Convertidor()
        self.puerto_serie = PuertoSerie()
        self.tarea.start()

    def prender_led(self, estado):
        print("SE PRENDERA EL LED")
        if estado:
            mensaje = self.convertidor.generar_mensaje(CONTROL, MOD_BANDERA, [0, 1])
        else:
            mensaje = self.convertidor.generar_mensaje(CONTROL, MOD_BANDERA, [1, 1])
        print(f"El mensaje a enviar es: {mensaje}  ", ' '.join('{0:02X}'.format(e) for e in mensaje))
        valor = self.puerto_serie.enviar_mensaje(mensaje)

    def run_controlador(self):
        print('Iniciando una operación superimportante')
        self.puerto_serie.abrir()
        self.funcionando = True
        while self.funcionando:
            print(f"LED {self.nombre}: ", self.led)
            self.contador += 1
            if self.worker:
                self.worker.senal_parpadeo(self.led)
                # valor = self.puerto_serie.enviar_mensaje(49, 49)
                # self.worker.senal_texto_temperatura(valor.decode())
            time.sleep(1)
            self.led = True

            print(f"LED {self.nombre}: ", self.led)
            if self.worker:
                self.worker.senal_parpadeo(self.led)

            time.sleep(1)
            self.led = False
        self.puerto_serie.cerrar()

    def establecer_worker(self, worker):
        self.worker = worker
        
    def detener(self):
        self.funcionando = False

        if self.tarea:
            self.tarea.join()
        print("Se ha detenido")


def main():
    controlador1 = Controlador("1")
    # controlador1.start()

    # controlador2 = Controlador("2")
    # controlador2.start()


if __name__=="__main__":
    main()