from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont


class ConvertButton(QPushButton):
    def __init__(self, window, runcon):
        super().__init__("Convert", window)
        self.clicked.connect(runcon)
        self.setFont(QFont("SF Pro", 10, QFont.Black))
        self.resize(385, 70)
        self.move(10, 235)
        self.show()
