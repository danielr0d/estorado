from pydub import AudioSegment

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QLineEdit, QPushButton, QFileDialog, QRadioButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QPixmap

from time import sleep
from threading import Thread
import sys

from src.components.convert_button import ConvertButton

app = QApplication(sys.argv)

my_pixmap = QPixmap("src/res/icon.jpg")
my_icon = QIcon(my_pixmap)

window = QWidget()

window.setWindowIcon(my_icon)

window.setGeometry(0, 0, 405, 370)
window.setFixedSize(window.size())
window.setWindowTitle("ESTORADO")


def openfile():
    global fl
    options = QFileDialog.Options()  # need to fix this bitch
    fileName, _ = QFileDialog.getOpenFileName(window, "Choose File", "", "Sound Files (*.mp3)", options=options)
    if fileName:
        fl = fileName
        btn.setText(fl)


def status():
    stat.setStyleSheet('color: green')
    stat.setText("Done!")
    sleep(1)
    stat.setText("Idle")


def runcon():
    Thread(target=convert).start()


def convert():
    dbs = txt.text()
    db = int(dbs)
    lowpassfreq = slider.value()
    (lowpassfreq)
    sound = AudioSegment.from_mp3(fl)
    sndloud = sound + db
    stat.setStyleSheet('color: green')
    stat.setText("Converting...")
    if b1.isChecked():
        sndboosted = sndloud.low_pass_filter(lowpassfreq)
        sndboostedb = sndboosted + db
        sndboostedb.export("Estorado.mp3", format='mp3')
    elif b2.isChecked():
        sndboosted = sndloud.low_pass_filter(lowpassfreq)
        sndboosted2 = sndboosted.low_pass_filter(lowpassfreq)
        sndboosted2b = sndboosted2 + db
        sndboosted2b.export("Estorado.mp3", format='mp3')
    elif b3.isChecked():
        sndboosted = sndloud.low_pass_filter(lowpassfreq)
        sndboosted2 = sndboosted.low_pass_filter(lowpassfreq)
        sndboosted3 = sndboosted2.low_pass_filter(lowpassfreq)
        sndboosted3b = sndboosted3 + db
        sndboosted3b.export("Estorado.mp3", format='mp3')
    else:
        pass

    status()


btn = QPushButton("Choose File (MP3 Only)", window)
btn.clicked.connect(openfile)

sett = QLabel("Settings", window)
sett.move(10, 100)
sett.setFont(QFont("SF Pro", 12, QFont.Black))
sett_width = 100  # Set this to the width of your QLabel
sett_height = 60  # Set this to the height of your QLabel

window_width = window.frameGeometry().width()
window_height = window.frameGeometry().height()

x = (window_width - sett_width) / 2
y = sett_height

sett.setGeometry(x, y, sett_width, sett_height)
sett.show()

lp = QLabel("Lowpass Cutoff (Hz):", window)
lp.move(10, 130)
lp.setFont(QFont("SF Pro", 11, QFont.Black))
lp.show()

slider = QSlider(Qt.Horizontal, window)
slider.setFocusPolicy(Qt.StrongFocus)
slider.setTickInterval(2250)
slider.move(175, 130)
slider.setMaximum(5000)
slider.setMinimum(500)
slider.setValue(2755)
slider.setTickPosition(slider.tickPosition())
slider.show()
slider.resize(218, 23)

nb3 = QLabel("500", window)
nb3.move(166, 118)
nb3.setFont(QFont("SF Pro", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

nb3 = QLabel("2250", window)
nb3.move(270, 118)
nb3.setFont(QFont("SF Pro", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

nb3 = QLabel("5000", window)
nb3.move(374, 118)
nb3.setFont(QFont("SF Pro", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

lpsd = QLabel("dB Increase: ", window)
lpsd.move(10, 157)
lpsd.setFont(QFont("SF Pro", 11, QFont.Black))
lpsd.show()

plus = QLabel("+", window)
plus.move(260, 161)
plus.setFont(QFont("SF Pro", 9, QFont.Black))
plus.show()

txt = QLineEdit(window)
txt.setText("50")
txt.resize(80, 20)
txt.move(270, 158)
txt.show()

b1 = QRadioButton("x1", window)
b1.setChecked(True)
b1.move(166, 187)
b1.show()

b2 = QRadioButton("x2", window)
b2.setChecked(False)
b2.move(260, 187)
b2.show()

b3 = QRadioButton("x3", window)
b3.setChecked(False)
b3.move(364, 187)
b3.show()

btn2 = ConvertButton(window, runcon)

nb3 = QLabel("FILE WILL BE EXPORTED ON estorado.py LOCATION", window)
nb3.move(10, 310)
nb3.setFont(QFont("SF Pro", 8, QFont.Black))
nb3.setStyleSheet('color: red')
nb3.show()

st = QLabel("Status:", window)
st.move(10, 330)
st.setFont(QFont("SF Pro", 12, QFont.Black))
st.show()

stat = QLabel("Idle                                                  ", window)
stat.move(80, 330)
stat.setFont(QFont("SF Pro", 12, QFont.Black))
stat.setStyleSheet('color: green')
stat.show()

dev = QLabel("Developed with weed, by danieo 🍁", window)
dev.move(235, 350)
dev.setFont(QFont("SF Pro", 8, QFont.Black))
dev.show()

d = QLabel("Filter Multiplier:", window)
d.move(10, 185)
d.setFont(QFont("SF Pro Display", 11, QFont.Black))
d.show()

window.show()

sys.exit(app.exec())
