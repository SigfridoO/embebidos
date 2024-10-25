from PyQt6.QtWidgets import QApplication
import sys

from Ventana import Ventana
from Servidor import ServidorSocket

class Inicio(Ventana):
    def __init__(self):
        super().__init__()

        servidor = ServidorSocket()
        self.establecer_servidor(servidor)
    



def main():
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()