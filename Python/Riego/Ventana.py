from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import Qt, QObject, QRunnable, QThreadPool, pyqtSignal as Signal
from PyQt6.QtGui import QFont, QPixmap, QCloseEvent
import sys
from pathlib import Path

from Controlador import Controlador

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Caja(QLabel):
    def __init__(self, color:str=""):
        super().__init__()
        self.setStyleSheet(f"Background-color:{color}")

class WorkerSignals(QObject):
    parpadeo = Signal(bool)
    texto_temperatura = Signal(str)
    
    def __init__(self) -> None:
        super().__init__()

class Worker(QRunnable):        
    def __init__(self) -> None:
        super().__init__()
        self.signals:WorkerSignals = WorkerSignals()

    def run(self):
        pass

    def senal_parpadeo(self, estado:bool = False):
        try:
            self.signals.parpadeo.emit(estado)
        except Exception as e:
            print(e)

    def senal_texto_temperatura(self, texto:str = ""):
        try:
            self.signals.texto_temperatura.emit(texto)
        except Exception as e:
            print(e)

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
        self.caja9 = Caja("blue")
        etiqueta_temperatura = QLabel("Temperatura")
        self.valor_temperatura = QLabel("")
        self.valor_temperatura.setStyleSheet(f"background-color: #FFFFFF; \
                                             border: 1px solid black")

        self.etiqueta_inidicador_encendido = QLabel()
        self.etiqueta_inidicador_encendido.setFixedSize(30, 30)

        self.etiqueta_inidicador_apagado = QLabel()
        self.etiqueta_inidicador_apagado.setFixedSize(30, 30)

        etiqueta_encender= QPushButton("Encender")
        etiqueta_apagar= QPushButton("Apagar")

        boton_aceptar = QPushButton("Aceptar")
        boton_cancelar = QPushButton("Cancelar")

        self.boton_led = QPushButton("LED")
        self.boton_led.setCheckable(True)
      
        layout_vertical1.addLayout(layout_superior)
        layout_vertical1.addLayout(layout_inferior)

        layout_superior.addWidget(self.etiqueta_inidicador_encendido, 0, 0)
        layout_superior.addWidget(self.etiqueta_inidicador_apagado, 1, 0)
        layout_superior.addWidget(etiqueta_encender, 0, 1, 1, 1)
        layout_superior.addWidget(etiqueta_apagar, 1, 1, 1, 1)
        layout_superior.addWidget(caja5, 0, 2, 2, 1)
        layout_superior.addWidget(self.boton_led, 2, 0, 1, 2)
        layout_superior.addWidget(self.caja9, 2, 2, 1, 1)
        layout_superior.addWidget(etiqueta_temperatura, 3, 0, 1, 2)
        layout_superior.addWidget(self.valor_temperatura, 3, 2, 1, 1)

        layout_inferior.addWidget(boton_aceptar)
        layout_inferior.addWidget(boton_cancelar)

        widget = QWidget()
        widget.setLayout(layout_vertical1)
        self.setCentralWidget(widget)
        self.setFixedSize(350, 200)

        self.threadpool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.parpadeo.connect(self.parpadear)
        self.worker.signals.texto_temperatura.connect(self.escribir_cuadro)

        self.threadpool.start(self.worker)

        self.mi_controlador = None

        #condiciones iniciales
        self.cambiar_estado_boton(self.etiqueta_inidicador_encendido, False)
        self.cambiar_estado_boton(self.etiqueta_inidicador_apagado, False)

        #listeners
        etiqueta_encender.clicked.connect(self.cambiar_boton_encender)
        etiqueta_encender.setCheckable(True)

        etiqueta_apagar.clicked.connect(self.cambiar_boton_apagar)
        etiqueta_apagar.setCheckable(True)

        self.boton_led.clicked.connect(self.prender_led)

    def cambiar_boton_encender(self, valor):
        self.cambiar_estado_boton(self.etiqueta_inidicador_encendido, valor)

    def cambiar_boton_apagar(self, valor):
        self.cambiar_estado_boton(self.etiqueta_inidicador_apagado, valor)

    def prender_led(self, estado):
        print("Encendiendo el led")

        if self.mi_controlador:
            self.mi_controlador.prender_led(estado)


    def cambiar_estado_boton(self, boton, estado):
        color = "red"
        if estado:
            color = 'green'

        boton.setStyleSheet(
            f"""Border: 1px solid {color}; 
            border-radius: 15px;
            background-color: {color};
            """)
    
    def parpadear(self, estado: bool):
        self.caja9.setHidden(not estado)
    
    def escribir_cuadro(self,  texto:str):
        self.valor_temperatura.setText(texto)

    def obtener_worker(self):
        return self.worker
    
    def establecer_controlador(self, controlador):
        self.mi_controlador = controlador

    def closeEvent(self, event:QCloseEvent):
        print("SE presiono el boton cerrar")
        if self.mi_controlador:
            self.mi_controlador.detener()

def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
