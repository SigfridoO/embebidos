from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QGridLayout,\
    QStatusBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QAction, QIcon
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
        self.setStatusBar(QStatusBar(self))
        self.construir_menu()
        self.resize(400, 300)

    def construir_menu(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu("&Archivo")
        menu_archivo.addAction("Abrir")

        menu_editar = menu.addMenu("&Editar")

        action_cortar = QAction("Cortar", self)
        action_cortar.triggered.connect(self.mostrar_mensaje)
        icono_cortar = QIcon(abs_path("rain122923.ico"))
        action_cortar.setIcon(icono_cortar)
        action_cortar.setShortcut("Ctrl+h")
        menu_editar.addAction(action_cortar)
        action_cortar.setStatusTip("Un comando para cortar información")

        menu_ayuda = menu.addMenu("A&yuda")

    def mostrar_mensaje(self):
        print("Mostrando mensaje")

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
