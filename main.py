from PyQt5.QtWidgets import QApplication
from gui import BibliotecaApp

def main():
    app = QApplication([])
    ventana_biblioteca = BibliotecaApp()
    ventana_biblioteca.show()
    app.exec_()

if __name__ == "__main__":
    main()

