from PyQt6.QtWidgets import QMainWindow, QPushButton

from src.new_connect.NewConnectWindow import NewConnectWindow



class Window(QMainWindow):
    def __init__(self, title: str = 'Redis Time Series'):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(1080, 720)
        self.setUpdatesEnabled(True)
        self.add_connect_button()
        self.w = None


    def add_connect_button(self):
        self.button = QPushButton("New Connection", self)
        self.button.resize(150, 45)
        self.button.move(10, 10)
        self.button.clicked.connect(self.show_new_window)


    def show_new_window(self):
        if self.w is None:
            w = NewConnectWindow(parent=self)
            w.show()

            def closeEvent(event):
                self.w = None

            w.closeEvent = closeEvent
            self.w = w



