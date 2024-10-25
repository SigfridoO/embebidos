from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QPushButton, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, \
    QComboBox, QWidget, \
    QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt6.QtCore import Qt, QObject, QRunnable, QThreadPool, pyqtSignal as Signal
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

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

        self.servidor = None
        self.boton = QPushButton("conectar")

        self.setCentralWidget(self.boton)

        self.resize(300, 250)


        self.boton.clicked.connect(self.iniciar_comunicacion)
        
    def iniciar_comunicacion(self):
        if self.servidor:
            self.servidor.establecerDireccion('192.168.0.216', 8000)


    def establecer_servidor(self, servidor):
        self.servidor = servidor


def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
