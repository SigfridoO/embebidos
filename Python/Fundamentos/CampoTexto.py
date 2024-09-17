from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.campo_texto = QLineEdit()

        self.setCentralWidget(self.campo_texto)
        self.campo_texto.textChanged.connect(self.texto_cambiado)
        self.campo_texto.returnPressed.connect(self.texto_presionado)
        self.setFixedSize(300, 150)

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
