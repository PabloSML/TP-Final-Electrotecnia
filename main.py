from src.interface import myWidget
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    window = myWidget()
    window.show()
    app.exec()
