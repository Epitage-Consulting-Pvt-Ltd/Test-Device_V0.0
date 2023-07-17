from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


# Declarations
btn_size_normal = (90, 40)
btn_size_big = (100, 50)

def create_button(text, parent, position, size, clicked_slot):
    button = QPushButton(text, parent)
    button.move(*position)
    button.setFixedSize(*size)
    button.clicked.connect(clicked_slot)
    return button


def create_labeled_textbox(label_text, parent, label_position, textbox_position, textbox_size):
    label = QLabel(label_text, parent)
    label.move(*label_position)
    label.setParent(parent)

    textbox = QLineEdit(parent)
    textbox.move(*textbox_position)
    textbox.resize(*textbox_size)
    textbox.setEnabled(True)
    textbox.setParent(parent)

    label.show()
    textbox.show()

    return label, textbox



def create_img_button(parent, image_path, size, position, on_click):
    img_btn = QPushButton(parent)
    pixmap = QPixmap(image_path)
    scaled_pixmap = pixmap.scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio)
    icon = QIcon(scaled_pixmap)
    img_btn.setIcon(icon)
    img_btn.setIconSize(scaled_pixmap.size())
    img_btn.move(*position)
    img_btn.setFixedSize(size, size)
    img_btn.clicked.connect(on_click)
    img_btn.show()
    return img_btn

# self.thumb_btn = create_thumb_button(self, 'images/userMainThumb.jpg', 120, (330, 600), self.close)

from PyQt5 import QtWidgets, QtCore, QtGui
import csv

class Completer(QtWidgets.QCompleter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

def load_combobox_with_autofill(combobox, filepath, column_name, autofill_textbox):
    combobox.clear()
    combobox.setEditable(True)

    completer = Completer(combobox)
    combobox.setCompleter(completer)
    #combobox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)

    wordlist = ["name"]  # Placeholder text

    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        available_columns = [column.strip() for column in reader.fieldnames]
        print("Available columns:", available_columns)
        for row in reader:
            wordlist.append(row[column_name.strip()])

    model = QtCore.QStringListModel(wordlist)
    combobox.setModel(model)


    combobox.currentIndexChanged.connect(lambda index: update_autofill_textbox(index, combobox, filepath, column_name, autofill_textbox))

def update_autofill_textbox(index, combobox, filepath, search_column, autofill_textbox):
    if index > 0:  # Skip the placeholder item
        selected_name = combobox.currentText()
        selected_row = get_row_from_csv(filepath, search_column, selected_name)
        if selected_row is not None:
            autofill_textbox.setText(selected_row['EmpId'])
        else:
            autofill_textbox.clear()
    else:
        autofill_textbox.clear()

def get_row_from_csv(filepath, search_column, search_value):
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[search_column] == search_value:
                return row
    return None
