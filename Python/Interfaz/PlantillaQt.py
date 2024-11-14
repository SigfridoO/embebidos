from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print('Creando la ventana')

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
