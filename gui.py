import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
)

class BibliotecaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sistema Biblioteca')
        self.setGeometry(100, 100, 800, 600)
        
        self.initUI()

    def initUI(self):
        # Widgets principales
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_principal = QVBoxLayout()
        self.central_widget.setLayout(self.layout_principal)

        # Botones de navegación
        self.btn_libros = QPushButton('Libros')
        self.btn_socios = QPushButton('Socios')
        self.btn_prestamos = QPushButton('Préstamos')
        self.btn_salir = QPushButton('Salir')

        self.layout_principal.addWidget(self.btn_libros)
        self.layout_principal.addWidget(self.btn_socios)
        self.layout_principal.addWidget(self.btn_prestamos)
        self.layout_principal.addWidget(self.btn_salir)

        # Eventos de botones
        self.btn_libros.clicked.connect(self.mostrar_interfaz_libros)
        self.btn_socios.clicked.connect(self.mostrar_interfaz_socios)
        self.btn_prestamos.clicked.connect(self.mostrar_interfaz_prestamos)
        self.btn_salir.clicked.connect(self.salir_aplicacion)

    def mostrar_interfaz_libros(self):
        self.limpiar_interfaz()
        # Implementar la interfaz para libros aquí

    def mostrar_interfaz_socios(self):
        self.limpiar_interfaz()
        # Implementar la interfaz para socios aquí

    def mostrar_interfaz_prestamos(self):
        self.limpiar_interfaz()
        # Implementar la interfaz para préstamos aquí

    def limpiar_interfaz(self):
        for i in reversed(range(self.layout_principal.count())):
            widget = self.layout_principal.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def salir_aplicacion(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_principal = BibliotecaApp()
    ventana_principal.show()
    sys.exit(app.exec_())

