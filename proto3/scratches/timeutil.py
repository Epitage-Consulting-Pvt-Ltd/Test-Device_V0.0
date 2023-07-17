from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer
from datetime import datetime
import sys

def timeqt(window,width, height):

    def update_date_time(label):
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

        # Update date and time label
        current_datetime_str = f"{formatted_date} - {formatted_time}"
        label.setText(current_datetime_str)




    # Create label for date and time
    date_time_label = QLabel(window)
    date_time_label.setGeometry(3, 3, 160, 20)

    # Set font for date and time label
    font_small = QFont("inika", 15, QFont.Bold)
    date_time_label.setFont(font_small)

    # Set font for date and time label
    font_big = QFont("inika", 20, QFont.Normal)

    timer = QTimer()
    timer.timeout.connect(lambda: update_date_time(date_time_label))
    timer.start(1000)

    # Initial date and time display
    update_date_time(date_time_label)


