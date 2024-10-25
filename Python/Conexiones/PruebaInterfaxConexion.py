from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QWidget, \
    QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

from ClienteSocket import ClienteSocket

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.direccion:str = ""
        self.puerto:int = 0

        self.cliente_socket = None


        self.boton = QPushButton("Conectar")


        self.campo_texto = QLineEdit()
        self.campo_texto.setPlaceholderText("Escribe algo")

        widget = QWidget()


        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        layout.addWidget(self.campo_texto)
        layout.addWidget(self.boton)


        self.campo_texto.textChanged.connect(self.texto_cambiado)
        self.campo_texto.returnPressed.connect(self.texto_presionado)

        self.boton.clicked.connect(self.conectar)

        self.setFixedSize(300, 150)

    def conectar(self):
        self.direccion = self.campo_texto.text()
        print ("La dirección a la que se conectara es: ", self.direccion)
        self.cliente_socket = ClienteSocket(self.direccion, self.puerto)

    def texto_presionado(self):
        texto = self.campo_texto.text()
        self.setWindowTitle(texto)
        print(texto)

    def texto_cambiado(self, texto):
        
        print(texto)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
