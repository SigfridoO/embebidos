from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Caja(QLabel):
    def __init__(self, color:str=""):
        super().__init__()
        self.setStyleSheet(f"Background-color:{color}")
        

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layout_vertical1 = QVBoxLayout()
        layout_superior = QGridLayout()          
        layout_inferior = QHBoxLayout()

        caja1 = Caja("green")
        caja2 = Caja("white")
        caja3 = Caja("red")
        caja4 = Caja("orange")
        caja5 = Caja("gray")
        caja6 = Caja("pink")
        caja7 = Caja("magenta")
        caja8 = Caja("cyan")
        caja9 = Caja("blue")
      

        widget = QWidget()
        widget.setLayout(layout_vertical1)
        self.setCentralWidget(widget)
        self.setFixedSize(300, 150)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
