import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter, QPalette
import csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QToolButton, QProgressBar , QComboBox
from PyQt5.QtGui import QIcon, QPixmap

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

from utilities.components import imgbutton ,create_img_button_H

import sys
import os



class NewUserWindow(QMainWindow):
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

        self.backbtn = imgbutton(self, "images/icons/BackIcon.png", 30, 30, (5, 44), self.openUserMenu)

        # Function to get the employee info based on the selected employee ID
        def get_employee_info(employee_id):
            with open('data/EmpMaster-Epitage.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == employee_id:
                        return row[1], row[2]  # Return EmployeeName and Date of Birth

        # Parse column from CSV file
        column_list = []
        dob_dict = {}  # Dictionary to store EmployeeName and Date of Birth mapping
        with open('data/EmpMaster-Epitage.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                column_list.append(row[0])  # Append EmpID to column_list
                dob_dict[row[0]] = row[2]  # Store empID and Date of Birth mapping

        name_id = QLabel('ID:', self)
        name_id.move(18, 102)

        # Placeholder image path
        placeholder_image_path = "images/placeholderimg.png"

        # QLabel to display employee picture
        picture_label = QLabel(self)
        picture_label.setGeometry(369, 96, 94, 142)
        # picture_label.setStylesheet()
        picture_label.setPixmap(QPixmap(placeholder_image_path))
        picture_label.setScaledContents(True)

        combo = QComboBox(self)
        combo.addItems(column_list)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)
        combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

        combo.setStyleSheet("QComboBox { height: 35px; }")
        combo.move(108, 96)
        combo.setFixedWidth(255)
        combo.setFixedHeight(30)

        def combo_text_changed():
            selected_employee_id = combo.currentText()
            if selected_employee_id:
                employee_info = get_employee_info(selected_employee_id)
                if employee_info is not None:
                    employee_name, dob = employee_info
                    text_id.setText(str(employee_name))  # Display EmployeeName
                    text_dob.setText(dob)
                    # Update employee picture based on the selected ID
                    image_path = f'img/{selected_employee_id}.jpg'  # Replace with your image path
                    picture_label.setPixmap(QPixmap(image_path))
                    return
            text_id.clear()
            text_dob.clear()
            picture_label.setPixmap(QPixmap(placeholder_image_path))  # Show placeholder image if no ID selected

        combo.currentTextChanged.connect(combo_text_changed)

        label_id = QLabel('Name', self)
        label_id.move(18, 139)

        text_id = QLineEdit(self)
        text_id.setReadOnly(False)
        text_id.move(108, 134)
        text_id.resize(255, 30)

        label_photo = QLabel('Photo', self)
        label_photo.move(18,176)

        text_photo = QLineEdit(self)
        text_photo.setReadOnly(False)
        text_photo.move(108, 171)
        text_photo.resize(255, 30)

        label_dob = QLabel('Birth Date', self)
        label_dob.move(18, 213)

        text_dob = QLineEdit(self)
        text_dob.setReadOnly(False)
        text_dob.move(108, 208)
        text_dob.resize(255, 30)

        self.rfidcardbtn = imgbutton(self, "images/icons/RFIDcard.png", 100, 100, (17, 246), self.openUserMenu)
        label_rfid = QLineEdit(self)
        label_rfid.setReadOnly(False)
        label_rfid.move(128, 246)
        label_rfid.resize(350, 30)

        self.fingerbtn = imgbutton(self, "images/icons/fingerbtn.png", 100, 100, (17, 372), self.openUserMenu)
        label_fing = QLineEdit(self)
        label_fing.setReadOnly(False)
        label_fing.move(128, 372)
        label_fing.resize(355, 30)

        self.facebtn = imgbutton(self, "images/icons/facebtn.png", 100, 100, (17, 498), self.openUserMenu)
        label_face = QLineEdit(self)
        label_face.setReadOnly(False)
        label_face.move(128, 498)
        label_face.resize(355,200)

        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(10, 720, 460, 20)
        progress_bar.setValue(0)

        self.cancelbtn = imgbutton(self, "images/icons/facebtn.png", 100, 100, (17, 498), self.openUserMenu)
        self.okbtn = imgbutton(self, "images/icons/facebtn.png", 100, 100, (17, 498), self.openUserMenu)


        self.show()

    def openUserMenu(self):
        from ..UserMenu import UserWindow
        self.openUserMenu = UserWindow()
        self.openUserMenu.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewUserWindow()
    window.show()
    sys.exit(app.exec_())






