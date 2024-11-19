from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, QMessageBox,  \
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

class BotonConSenal(QPushButton):
    def __init__(self, nombre, indice_encendido, indice_apagado):
        super().__init__()
        self.setText(nombre)
        self.indice_encendido = indice_encendido
        self.indice_apagado = indice_apagado
    

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

        self.boton_activar_wifi = BotonConSenal("Activar Wifi", 60, 61)
        self.boton_activar_wifi.setCheckable(True)

        self.boton_activar_socket = BotonConSenal("Activar Socket", 62, 63)
        self.boton_activar_socket.setCheckable(True)

        self.boton_activar_websocket = BotonConSenal("Activar Websocket", 64, 65)
        self.boton_activar_websocket.setCheckable(True)


        layout_temp = QGridLayout()
        widget_aux = QWidget()
        widget_aux.setLayout(layout_temp)
        etiqueta_m = QLabel("m")
        self.txt_m = QLineEdit()

        etiqueta_b = QLabel("b")
        self.txt_b = QLineEdit()

        self.boton_analog_conf = QPushButton("Enviar")
        layout_temp.addWidget(etiqueta_m, 0,0)
        layout_temp.addWidget(self.txt_m, 0,1)
        layout_temp.addWidget(etiqueta_b, 0,2)
        layout_temp.addWidget(self.txt_b, 0,3)
        layout_temp.addWidget(self.boton_analog_conf, 0,4)



        layout_vertical1.addLayout(layout_superior)
        layout_vertical1.addLayout(layout_inferior)

        layout_superior.addWidget(self.etiqueta_inidicador_encendido, 0, 0)
        layout_superior.addWidget(self.etiqueta_inidicador_apagado, 1, 0)
        layout_superior.addWidget(etiqueta_encender, 0, 1, 1, 1)
        layout_superior.addWidget(etiqueta_apagar, 1, 1, 1, 1)
        layout_superior.addWidget(caja5, 0, 2, 2, 1)
        layout_superior.addWidget(self.boton_led, 2, 0, 1, 2)
        layout_superior.addWidget(self.caja9, 2, 2, 1, 1)
        layout_superior.addWidget(self.boton_activar_wifi, 3, 0, 1, 2)
        layout_superior.addWidget(self.boton_activar_socket, 4, 0, 1, 2)
        layout_superior.addWidget(self.boton_activar_websocket, 5, 0, 1, 2)
        layout_superior.addWidget(etiqueta_temperatura, 6, 0, 1, 2)
        layout_superior.addWidget(self.valor_temperatura, 6, 2, 1, 1)
        layout_superior.addWidget(widget_aux, 7, 0, 1, 3)

        layout_inferior.addWidget(boton_aceptar)
        layout_inferior.addWidget(boton_cancelar)

        widget = QWidget()
        widget.setLayout(layout_vertical1)
        self.setCentralWidget(widget)
        self.resize(350, 320)

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

        self.boton_activar_wifi.clicked.connect(self.activar_senal_digital)
        self.boton_activar_socket.clicked.connect(self.activar_senal_digital)
        self.boton_activar_websocket.clicked.connect(self.activar_senal_digital)

    def cambiar_boton_encender(self, valor):
        self.cambiar_estado_boton(self.etiqueta_inidicador_encendido, valor)

    def cambiar_boton_apagar(self, valor):
        self.cambiar_estado_boton(self.etiqueta_inidicador_apagado, valor)

    def prender_led(self, estado):
        print("Encendiendo el led")

        if self.mi_controlador:
            self.mi_controlador.prender_led(estado)

    def activar_senal_digital(self, estado):
        # print("Encendiendo el led")
        boton = self.sender()
        if isinstance(boton, BotonConSenal):
            print(f"Encendiendo el led: indice_encendido={boton.indice_encendido}, indice_apagado={boton.indice_apagado}")

            if self.mi_controlador:
                self.mi_controlador.activar_senal(estado, boton.indice_encendido, boton.indice_apagado)


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
        respuesta = QMessageBox.question(self, 'Cerrar Aplicación',
                                    "¿Estás seguro de que quieres salir?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            if self.mi_controlador:
                self.mi_controlador.detener()
            event.accept()
        else:
            event.ignore()



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
