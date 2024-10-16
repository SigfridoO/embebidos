import time 
import threading

from PuertoSerie import PuertoSerie

class Controlador(threading.Thread):
    def __init__(self, nombre: str=""):
        super().__init__()
        print('Dentro del constructor de controlador')

        self.led_real =False
        self.led = False
        self.nombre = nombre

        self.worker = None

        self.contador = 0
        self.puerto_serie = PuertoSerie()

    def prender_led(self):
        print("SE PRENDERA EL LED")
        valor = self.puerto_serie.enviar_mensaje(49, 52)

    def run(self):
        print('Iniciando una operación superimportante')
        self.puerto_serie.abrir()
        while True:
            print(f"LED {self.nombre}: ", self.led)
            self.contador += 1
            if self.worker:
                self.worker.senal_parpadeo(self.led)
                valor = self.puerto_serie.enviar_mensaje(49, 49)
                self.worker.senal_texto_temperatura(valor.decode())
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
        


def main():
    controlador1 = Controlador("1")
    controlador1.start()

    # controlador2 = Controlador("2")
    # controlador2.start()


if __name__=="__main__":
    main()