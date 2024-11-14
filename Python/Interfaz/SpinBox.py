from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.campo_numerico = QDoubleSpinBox()
        self.campo_numerico.valueChanged.connect(self.valor_cambiado)
        self.campo_numerico.setRange(10, 40)
        self.campo_numerico.setSuffix("º")
        self.campo_numerico.setPrefix("Temp: ")
        self.campo_numerico.setSingleStep(0.5)

        fuente = QFont('Manjari', 36)
        self.campo_numerico.setFont(fuente)
        
        self.setCentralWidget(self.campo_numerico)
        self.setFixedSize(300, 150)

    def valor_cambiado(self, valor):
        print(valor)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
