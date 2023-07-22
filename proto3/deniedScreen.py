import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer, QDateTime, QPropertyAnimation
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout ,QHBoxLayout
from datetime import datetime
from utilities.components import *


class verifiedScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 480
        self.height = 800
        self.resize(480, 400)

        self.tick_label = QLabel(self)
        self.tick_label.setAlignment(Qt.AlignCenter)
        self.tick_label.setGeometry(40, 5, 480, 800)

        pixmap = QPixmap('images/icons/accessDeniedIcon.png')
        scaled_pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        tick_label = QLabel(self.tick_label)
        tick_label.setPixmap(scaled_pixmap)
        tick_label.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.show()

    def show_verified_animation(self):
            self.tick_label.show()
            #self.tick_label.setOpacity(0.0)

            animation = QPropertyAnimation(self.tick_label, b'opacity', self)
            animation.setDuration(1000)  # Duration of the animation in milliseconds
            animation.setStartValue(0.0)
            animation.setEndValue(1.0)

            animation.start(QPropertyAnimation.DeleteWhenStopped)

            # Optionally, you can close the window automatically after the animation finishes
            QTimer.singleShot(1500, self.close)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = verifiedScreen()
    window.show_verified_animation()
    sys.exit(app.exec_())
