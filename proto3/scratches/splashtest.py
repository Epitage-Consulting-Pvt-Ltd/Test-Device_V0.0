import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from timeutil import timeqt
class DisplayWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        timeqt(DisplayWindow,width=480,height=800)

        font_big = QFont("inika", 20, QFont.Normal)
        # Create label for additional date
        self.additional_date_label = QLabel(self)
        self.additional_date_label.setGeometry(137, 509, 300,26)
        self.additional_date_label.setFont(font_big)
        self.additional_date_label.setAlignment(Qt.AlignVCenter)

        # Create label for time
        self.time_label = QLabel(self)
        self.time_label.setGeometry(207, 547, 300, 30)
        self.time_label.setFont(font_big)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayWindow()
    window.show()
    sys.exit(app.exec_())
