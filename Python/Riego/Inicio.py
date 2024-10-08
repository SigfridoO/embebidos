from PyQt6.QtWidgets import QApplication
import sys

from Ventana import Ventana
from Controlador import Controlador

class Inicio(Ventana):
    def __init__(self):
        super().__init__()

        
        controlador1 = Controlador("1")
        controlador1.start()
        controlador1.establecer_worker(self.obtener_worker())

def main():
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
