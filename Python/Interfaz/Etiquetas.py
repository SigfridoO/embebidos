from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre )

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        print('Creando la ventana')
        mi_etiqueta = QLabel("Saludos")
        mi_etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter \
                                 | Qt.AlignmentFlag.AlignVCenter)
        fuente = QFont('Manjari', 24)
        mi_etiqueta.setFont(fuente)
        #print(abs_path("lemur.jpg"))
        imagen = QPixmap(abs_path("lemur.jpg"))
        mi_etiqueta.setPixmap(imagen)
        mi_etiqueta.setScaledContents(True)

        self.setCentralWidget(mi_etiqueta)
        self.setFixedSize(400, 300)


def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
