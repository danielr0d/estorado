from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont


class ChooseButton(QPushButton):
    def __init__(self, window, openfile):
        super().__init__("Choose File (MP3 Only)", window)
        self.clicked.connect(openfile)
        self.setFont(QFont("SF Pro", 10, QFont.Black))
        self.move(9, 30)
        self.resize(385, 30)
        self.show()


