from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.combo = QComboBox()
        self.combo.addItems( ["", "Opción 1", "Opción 2", "Opcion 3"])
        self.combo.currentTextChanged.connect(self.cambiar_texto)
        self.combo.currentIndexChanged.connect(self.cambiar_indice)

        self.setCentralWidget(self.combo)
        self.setFixedSize(300, 150)

    def cambiar_texto(self, texto):
        print(texto)

    def cambiar_indice(self, indice):
        print(type(indice), indice)



def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
