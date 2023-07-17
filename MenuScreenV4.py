
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow ,QPushButton , QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from datetime import datetime
from utilities.components import create_img_button , create_labeled_textbox , imgbutton
from splashscreenv4 import SplashWindow


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window dimensions
        self.width = 480
        self.height = 800
        self.setGeometry(0, 0, self.width, self.height)

        # Set background image
        self.background_image = QLabel(self)
        self.background_image.setPixmap(QPixmap("images/background.png"))
        self.background_image.setGeometry(0, 0, self.width, self.height)

        # Create label for date and time
        self.date_time_label = QLabel(self)
        self.date_time_label.setGeometry(3, 3, 160, 20)

        # Set font for date and time label
        font_small = QFont("inika", 15, QFont.Bold)
        self.date_time_label.setFont(font_small)

        # Initial date and time display
        self.update_date_time()

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

        self.backbtn = imgbutton(self, "images/icons/BackIcon.png", 30,30, (5, 44), self.openSplashScreen)

        # Create the label
        label = QLabel("Password", self)
        label.setStyleSheet("color: #808080")
        label.move(18, 106)

        # Create the password field
        self.password_field = QLineEdit(self)
        self.password_field.setPlaceholderText("here")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.textChanged.connect(self.verify_password)
        self.password_field.setFixedSize(355, 30)
        self.password_field.move(108, 100)

        #self.passwordfield2 = create_labeled_textbox("Password",self,(18,106),(108,100),(355,30),"here")



        self.deviceMenu = create_img_button(self,"images/icons/DeviceIcon.png", 55, 100, (18, 142), self.close, "Device", "#D9D9D9")
        self.deviceMenu.setEnabled(False)

        self.UserMenu = create_img_button(self, "images/icons/UserIcon.png", 55, 100, (133, 142), self.openUserScreen,"User", "#D9D9D9")
        self.UserMenu.setEnabled(False)

        self.CommMenu = create_img_button(self, "images/icons/CommIcon.png", 55, 100, (248, 142), self.close,"Comm", "#D9D9D9")
        self.CommMenu.setEnabled(False)

        self.LogMenu = create_img_button(self, "images/icons/DeviceIcon.png", 55, 100, (363, 142), self.close,"Log","#D9D9D9")
        self.LogMenu.setEnabled(False)

        self.PrinterMenu = create_img_button(self, "images/icons/printerIcon.png", 55, 100, (18, 264), self.close,"Printer","#D9D9D9")
        self.PrinterMenu.setEnabled(False)

        self.VerifyButton = create_img_button(self, "images/icons/UserVerifyIcon.png", 55, 100, (133, 264), self.UserVerification,"Verify User","#D9D9D9")
        self.VerifyButton.setEnabled(False)


    def verify_password(self):
        password = self.password_field.text()
        print("Entered Password:", password)

        # Perform password verification logic here
        # For example, check if the password matches a predefined value
        expected_password = "admin"
        is_password_matched = (password == expected_password)
        print("Password Matched:", is_password_matched)

        # Enable or disable buttons based on password verification result
        self.deviceMenu.setEnabled(is_password_matched)
        self.UserMenu.setEnabled(is_password_matched)
        self.CommMenu.setEnabled(is_password_matched)
        self.LogMenu.setEnabled(is_password_matched)
        self.VerifyButton.setEnabled(is_password_matched)

    def openUserScreen(self):
        from UserMenu import UserWindow
        self.openUserScreen = UserWindow()
        self.openUserScreen.show()
        self.close()

    def openSplashScreen(self):
        from splashscreenv4 import SplashWindow
        self.openSplashScreen = SplashWindow()
        self.openSplashScreen.show()
        self.close()

    def UserVerification(self):
        from userverification import CardVerificationApp
        self.UserVerification = CardVerificationApp()
        self.UserVerification.show()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())






