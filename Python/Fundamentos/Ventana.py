from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton
import sys

"""
    Este es un
    bloque de comentario
"""
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print('Creando la ventana')
        boton = QPushButton("Presioname")
        boton.clicked.connect(self.clickear)
        boton.released.connect(self.liberar)
        boton.pressed.connect(self.presionar)

        self.setCentralWidget(boton)

    def clickear(self):
        print ("Se ha clickeado el botón")

    def presionar(self):
        print ("Se ha presionado el botón")

    def liberar(self):
        print ("Se ha liberado el botón")

def main():
    print('Dentro de main')
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
