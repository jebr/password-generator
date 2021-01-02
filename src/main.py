import os
import sys
import pyperclip

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui

import passgen as pg
import uifunc as uf

# Software version
current_version = float(1.0)

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
    # logging.info('Pyinstaller file location {}'.format(base_path))
    return os.path.join(base_path, relative_path)

DUTCH_DICT = resource_path('resources/dictionaries/wordlist_dutch.json')
ENGLISH_DICT = resource_path('resources/dictionaries/wordlist_english.json')
A_Z_CAPITAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A_Z_LOWER = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS1 = "#$%@^`~"
SYMBOLS2 = ".,:;"
SYMBOLS3 = "\"\'"
SYMBOLS4 = "\\/|_-"
SYMBOLS5 = "<*+!?="
SYMBOLS6 = "{[()]}"

ui_main_window = resource_path('resources/ui/main_window.ui')
icon_app_logo = resource_path('icons/password-generator-icon.ico')
# icon_generate_password = resource_path()
# icon_copy_password = resource_path()


class MainPage(QtWidgets.QMainWindow, uf.UiFunc):
    def __init__(self):
        super().__init__()
        loadUi(ui_main_window, self)
        # self.setFixedSize(900, 850)
        self.setWindowIcon(QtGui.QIcon(icon_app_logo))
        # Pushbuttons
        self.pb_generate.clicked.connect(self.create_password)
        self.pb_copy.clicked.connect(self.copy_password)
        # Sliders and spinboxes
        self.slider_password.valueChanged.connect(self.password_slider_value_changed)
        self.spin_password.valueChanged.connect(self.password_spin_value_changed)

    def create_password(self):
        chars = []
        if self.check_az_capital.isChecked():
            chars.append(A_Z_CAPITAL)
        if self.check_az_lower.isChecked():
            chars.append(A_Z_LOWER)
        if self.check_numbers.isChecked():
            chars.append(NUMBERS)
        if self.check_symbols1.isChecked():
            chars.append(SYMBOLS1)
        if self.check_symbols2.isChecked():
            chars.append(SYMBOLS2)
        if self.check_symbols3.isChecked():
            chars.append(SYMBOLS3)
        if self.check_symbols4.isChecked():
            chars.append(SYMBOLS4)
        if self.check_symbols5.isChecked():
            chars.append(SYMBOLS5)
        if self.check_symbols6.isChecked():
            chars.append(SYMBOLS6)

        characters = str.join('', chars)
        length = self.slider_password.value()
        password = pg.PasswordGenerator.create_password(length, characters)
        self.line_generated_password.setText(password)

    def create_passphrase(self):
        pass

    def copy_password(self):
        pyperclip.copy(self.line_generated_password.text())

    def password_slider_value_changed(self):
        slider_value = self.slider_password.value()
        self.spin_password.setValue(slider_value)
        self.create_password()

    def password_spin_value_changed(self):
        spin_value = self.spin_password.value()
        self.slider_password.setValue(spin_value)
        self.create_password()

def main():
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

