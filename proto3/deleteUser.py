import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit, QCheckBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime
from datetime import datetime
from utilities.components import *


class copyUser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 480
        self.height = 800
        self.resize(480, 800)

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        self.copyUser = imgbutton2(self, "images/icons/copyUserIcon50x50.png", 50, 50, [215, 34], self.close)
        self.copyUser.setEnabled(False)

        self.backbtnv2 = imgbutton2(self, "images/icons/BackIcon.png", 30, 30, (5, 44), self.close)


        cancel_btn = imgbutton2(self, "images/icons/Cancel_btn.png", 100, 100, [147, 729], self.close)
        cancel_btn.resize(85,35)

        copy_btn = imgbutton2(self, "images/icons/copyBtn.png", 100, 100, [248, 729], self.close)
        copy_btn.resize(85,35)

        #labels & textfields

        label = QLabel("ID", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 101)

        self.ID_field = QLineEdit(self)
        self.ID_field.setFixedSize(355, 30)
        self.ID_field.move(108, 96)

        label = QLabel("Card", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 140)
        # checkbox for Card
        self.cardCheckbox = QCheckBox(self)
        self.cardCheckbox.setGeometry(108, 135, 100, 40)
        self.cardCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.cardCheckbox.move(108, 135)

        label = QLabel("Thumb", self)
        label.setStyleSheet("color: #808080")
        label.move(158, 140)
        # checkbox for Thumb
        self.thumbCheckbox = QCheckBox(self)
        self.thumbCheckbox.setGeometry(223, 135, 100, 40)
        self.thumbCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.thumbCheckbox.move(223, 135)

        label = QLabel("Face", self)
        label.setStyleSheet("color: #808080")
        label.move(278, 140)
        # checkbox for Face
        self.faceCheckbox = QCheckBox(self)
        self.faceCheckbox.setGeometry(321, 135, 100, 40)
        self.faceCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.faceCheckbox.move(321, 135)

        label = QLabel("Photo", self)
        label.setStyleSheet("color: #808080")
        label.move(382, 140)
        # checkbox for Photo
        self.photoCheckbox = QCheckBox(self)
        self.photoCheckbox.setGeometry(433, 135, 100, 40)
        self.photoCheckbox.setStyleSheet("QCheckBox::indicator""{""width : 20px;""height : 20px;""}"
                                        "QCheckBox::indicator:pressed""{""background-color : orange;""}")
        #self.photoCheckbox.move(433, 135)


        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(5, 4, 190, 20)

        # Set font for date and time label
        font_small = QFont("inika", 10, QFont.Normal)
        self.date_time_label.setFont(font_small)

        # Create label for time
        self.time_label = QLabel(self)
        self.time_label.setGeometry(195, 547, 300, 30)
        self.time_label.setFont(font_small)

        # Update date and time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)

        # Initial date and time display
        self.update_date_time()

    # to add condition for the checkboxes
    # def on_checkbox_state_change(state):
    #    if state == 2:  # 2 corresponds to Qt.Checked
    #        print("Checkbox is checked")
    #    else:
    #        print("Checkbox is unchecked")

    def openfoodMenu(self):
        from foodMenu import food_menu
        self.openfoodMenu = food_menu()
        self.openfoodMenu.show()
        self.close()

    def update_date_time(self):
        # Get current date and time
        current_datetime = datetime.now()

        # Format the date as "14th June 2023"
        formatted_date = current_datetime.strftime("%d{} %B %Y").format(
            "th" if 10 <= current_datetime.day <= 19 else
            {1: "st", 2: "nd", 3: "rd"}.get(current_datetime.day % 10, "th")
        )

        # Get the current day
        current_day = current_datetime.strftime("%A")

        # Format the time as "hh:mm:ss"
        formatted_time = current_datetime.strftime("%H:%M:%S")

        # Update date and time labels
        current_datetime_str = f"{formatted_date} - {formatted_time}"
        self.date_time_label.setText(current_datetime_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = copyUser()
    window.show()
    sys.exit(app.exec_())