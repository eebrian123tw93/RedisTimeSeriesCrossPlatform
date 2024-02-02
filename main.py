from PyQt6 import QtWidgets
import sys
from Ui_MainWindow import Ui_MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    ui_window = Ui_MainWindow()
    ui_window.setupUi(MainWindow=main_window)
    main_window.show()

    sys.exit(app.exec())