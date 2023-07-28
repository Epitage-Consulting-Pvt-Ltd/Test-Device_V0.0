import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from utilities.components import *


class togButton(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 480
        self.height = 800
        self.resize(480, 800)

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        self.toggle_but = QPushButton(self)
        self.toggle_but.setGeometry(17, 246, 100, 100)
        self.toggle_but.setCheckable(True)
        self.toggle_but.clicked.connect(self.toggle)
        icon = QIcon("images/icons/Card.png")
        self.toggle_but.setIcon(icon)
        icon_size = QSize(90, 90)
        self.toggle_but.setIconSize(icon_size)

    def toggle(self):
        if self.toggle_but.isChecked():

            self.toggle_but.setStyleSheet("QPushButton {background-color:lightgreen}")

        else:

            self.toggle_but.setStyleSheet("QPushButton {background-color:lightcoral}")


        #self.canteen = imgbutton2(self, "images/icons/Card.png", 100, 100, [17, 246], self.close)
        #self.canteen.setCheckable(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = togButton()
    window.show()
    sys.exit(app.exec_())
