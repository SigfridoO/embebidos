from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QKeyEvent, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Caja(QLabel):
    def __init__(self, color:str=""):
        super().__init__()
        self.setStyleSheet(f"Background-color:{color}")
        
class pantallaInicio(QWidget):
    def __init__(self):
        super().__init__()

        layout_horizontal = QHBoxLayout();
        boton_aceptar = QPushButton("Aceptar")
        boton_cancelar = QPushButton("Terminar")
        layout_horizontal.addWidget(boton_aceptar)
        layout_horizontal.addWidget(boton_cancelar)
        self.setLayout(layout_horizontal)
        


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
   
        self.layout = QStackedLayout()
        self.layout.addWidget(pantallaInicio())
        self.layout.addWidget(Caja("#456787"))
        self.layout.addWidget(Caja("#AAFECC"))
        self.layout.addWidget(Caja("#00FECC"))

        
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        self.layout.setCurrentIndex(1)
    
    def keyPressEvent(self, event: QKeyEvent | None) -> None:

        indice = self.layout.currentIndex()
        indice_maximo = self.layout.count()-1

        if event.key() == Qt.Key.Key_Right:
            indice -= 1

        if event.key() == Qt.Key.Key_Left:
            indice += 1

        if indice < 0:
            indice = indice_maximo
        if indice > indice_maximo:
            indice = 0
        self.layout.setCurrentIndex(indice)
        



def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
