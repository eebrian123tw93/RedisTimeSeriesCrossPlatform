from PyQt6 import QtWidgets
import sys
from src.Window import Window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())