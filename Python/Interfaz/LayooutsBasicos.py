from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QHBoxLayout, QVBoxLayout, QWidget
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

        layout = QVBoxLayout()
        layout_horizontal = QHBoxLayout()

        caja1 = Caja("green")
        #caja2 = Caja("white")
        caja3 = Caja("red")
        caja4 = Caja("orange")
        caja5 = Caja("white")
        caja6 = Caja("pink")

        layout_horizontal.addWidget(caja4)
        layout_horizontal.addWidget(caja5)
        layout_horizontal.addWidget(caja6)

        layout.addWidget(caja1)
        layout.addLayout(layout_horizontal)
        layout.addWidget(caja3)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        #self.setFixedSize(300, 150)



def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
