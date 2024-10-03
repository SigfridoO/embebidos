import time 
import threading

class Controlador(threading.Thread):
    def __init__(self, nombre: str=""):
        super().__init__()
        print('Dentro del constructor de controlador')
        self.led = False
        self.nombre = nombre

    def run(self):
        print('Iniciando una operación superimportante')
        while True:
            print(f"LED {self.nombre}: ", self.led)
            time.sleep(1)
            self.led = True

            print(f"LED {self.nombre}: ", self.led)
            time.sleep(1)
            self.led = False
            


def main():
    controlador1 = Controlador("1")
    controlador1.start()

    controlador2 = Controlador("2")
    controlador2.start()


if __name__=="__main__":
    main()