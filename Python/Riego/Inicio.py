from PyQt6.QtWidgets import QApplication
import sys

from Ventana import Ventana


def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()