from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRect


class NewConnectWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setWindowTitle("New Connection")
        self.resize(720, 480)

        self.h_layout = QHBoxLayout(self)
        self.h_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label = QLabel("New Connection", parent=self)
        self.h_layout.addWidget(self.label)

        self.close_button = QPushButton(parent=self)
        self.close_button.clicked.connect(self.close)
        self.h_layout.addWidget(self.close_button)

        # 鎖定Window
        self.setWindowFlag(Qt.WindowType.Window)
        self.setWindowModality(Qt.WindowModality.WindowModal)

