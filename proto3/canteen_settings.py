import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from datetime import datetime
from utilities.components import create_img_button , create_labeled_textbox , imgbutton


class canteen_settings(QMainWindow):
    def __init__(self):
        super().__init__()

        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)

        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        self.canteenMain = create_img_button(self, "images/icons/CanteenIcon.png", 100, 100, (18, 99), self.close, "Canteen", "#D9D9D9")
        self.canteenMain.setEnabled(False)

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

        self.backbtn = imgbutton(self, "images/icons/BackIcon.png", 30, 30, (5, 44))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = canteen_settings()
    window.show()
    sys.exit(app.exec_())
