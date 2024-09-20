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

        self.etiqueta_inidicador_encendido = QLabel()
        self.etiqueta_inidicador_encendido.setFixedSize(30, 30)

        etiqueta_inidicador_apagado = QLabel()
        etiqueta_inidicador_apagado.setFixedSize(30, 30)

        etiqueta_encender= QPushButton("Encender")
        etiqueta_apagar= QPushButton("Apagar")

        boton_aceptar = QPushButton("Aceptar")
        boton_cancelar = QPushButton("Cancelar")
      
        layout_vertical1.addLayout(layout_superior)
        layout_vertical1.addLayout(layout_inferior)

        layout_superior.addWidget(self.etiqueta_inidicador_encendido, 0, 0)
        layout_superior.addWidget(etiqueta_inidicador_apagado, 1, 0)
        layout_superior.addWidget(etiqueta_encender, 0, 1, 1, 1)
        layout_superior.addWidget(etiqueta_apagar, 1, 1, 1, 1)
        layout_superior.addWidget(caja5, 0, 2, 2, 1)
        layout_superior.addWidget(caja3, 2, 0, 1, 2)

        layout_inferior.addWidget(boton_aceptar)
        layout_inferior.addWidget(boton_cancelar)

        widget = QWidget()
        widget.setLayout(layout_vertical1)
        self.setCentralWidget(widget)
        self.setFixedSize(300, 150)

        #condiciones iniciales
        self.cambiar_estado_boton(self.etiqueta_inidicador_encendido, False)
        self.cambiar_estado_boton(etiqueta_inidicador_apagado, False)

        #listeners
        etiqueta_encender.clicked.connect(self.cambiar_boton_encender)
        etiqueta_encender.setCheckable(True)

    def cambiar_boton_encender(self, valor):
        self.cambiar_estado_boton(self.etiqueta_inidicador_encendido, valor)

    def cambiar_estado_boton(self, boton, estado):
        color = "red"
        if estado:
            color = 'green'

        boton.setStyleSheet(
            f"""Border: 1px solid {color}; 
            border-radius: 15px;
            background-color: {color};
            """)

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
