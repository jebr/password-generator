import os
import sys
import threading
import pyperclip
import webbrowser
import json
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence
from PyQt5.QtWidgets import QApplication, QShortcut, QDialog, QLabel
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore

import passgen as pg
import basicfunc as bf

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception as e:
    pass


def resource_path(relative_path):
    """ Get absolute path to resource, dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception as e:
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
ui_info_window = resource_path('resources/ui/info_dialog.ui')
ui_update_window = resource_path('resources/ui/update_window.ui')
icon_app_logo = resource_path('icons/password-generator-icon.ico')
icon_generate_password = resource_path(
    'icons/glyphicons-basic-82-refresh@3x.png')
icon_copy_password = resource_path('icons/glyphicons-basic-614-copy@3x.png')


# def software_version():
#     with open(resource_path('version.txt'), 'r') as version_file:
#         # version = json.load(version_file)
#         version = version_file.readline()
#         return float(version)

# Software version
current_version = 1.1
update_check_url = 'https://raw.githubusercontent.com/jebr/' \
                  'password-generator/main/version.txt'
release_url = "https://github.com/jebr/password-generator/releases"

def open_info_window():
    info_window_ = InfoWindow()
    info_window_.exec_()


def open_update_window(latest_version):
    update_window = UpdateWindow(latest_version)
    update_window.exec_()


def auto_update_check():
    check = bf.BasicFunc.update_check(update_check_url, current_version)
    if check == "no-connection":
        return
    elif check == "up-to-date":
        return
    else:
        open_update_window(check)


def open_download_link():
    try:
        webbrowser.open(release_url, new=1)
    except ImportError:
        pass


class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(ui_main_window, self)
        # self.setFixedSize(900, 850)
        self.setMinimumSize(760, 390)
        self.setWindowIcon(QtGui.QIcon(icon_app_logo))
        self.setWindowTitle("Password Generator")
        self.action_about.triggered.connect(open_info_window)
        # Pushbuttons
        self.pb_generate.clicked.connect(self.generate_passsword_button)
        self.pb_copy.clicked.connect(self.copy_password)
        self.pb_generate.setText("")
        self.pb_generate.setIcon(QIcon(QPixmap(icon_generate_password)))
        self.pb_copy.setText("")
        self.pb_copy.setIcon(QIcon(QPixmap(icon_copy_password)))
        # Password Sliders, spinboxes and checkboxes
        self.slider_password.valueChanged.connect(
            self.password_slider_value_changed)
        self.spin_password.valueChanged.connect(
            self.password_spin_value_changed)
        self.check_az_capital.stateChanged.connect(self.create_password)
        self.check_az_lower.stateChanged.connect(self.create_password)
        self.check_numbers.stateChanged.connect(self.create_password)
        self.check_symbols1.stateChanged.connect(self.create_password)
        self.check_symbols2.stateChanged.connect(self.create_password)
        self.check_symbols3.stateChanged.connect(self.create_password)
        self.check_symbols4.stateChanged.connect(self.create_password)
        self.check_symbols5.stateChanged.connect(self.create_password)
        self.check_symbols6.stateChanged.connect(self.create_password)
        # Passphrase Sliders, spinboxes and checkboxes
        self.slider_passphrase.valueChanged.connect(
            self.passphrase_slider_value_changed)
        self.spin_passphrase.valueChanged.connect(
            self.passphrase_spin_value_changed)
        self.combo_passphrase_seperator.currentIndexChanged.connect(
            self.create_passphrase)
        self.combo_passphrase_text.currentIndexChanged.connect(
            self.create_passphrase)
        self.combo_passphrase_lang.currentIndexChanged.connect(
            self.create_passphrase)
        self.check_passphrase_numbers.stateChanged.connect(
            self.create_passphrase)
        # Check current tabwidget on change between tabs
        self.tabWidget.currentChanged.connect(self.tabwidget_changed)
        # Init functions
        self.set_text_copy()
        self.lb_grade.setText("Kwaliteit: ")
        # Shortcuts for buttons
        self.generate_password_btn = QShortcut(QKeySequence('Return'), self)
        self.generate_password_btn.activated.connect(
            self.generate_passsword_button)
        self.copy_password_btn = QShortcut(QKeySequence('Ctrl+C'), self)
        self.copy_password_btn.activated.connect(self.copy_password)
        # Check if password is editted
        self.line_generated_password.textChanged.connect(
            self.check_password_strength)
        # Auto check for new updates
        auto_update_check()

    def create_password(self):
        chars = []
        count_length = 0
        if self.check_az_capital.isChecked():
            chars.append(A_Z_CAPITAL)
            count_length += 1
        if self.check_az_lower.isChecked():
            chars.append(A_Z_LOWER)
            count_length += 1
        if self.check_numbers.isChecked():
            chars.append(NUMBERS)
            count_length += 1
        if self.check_symbols1.isChecked():
            chars.append(SYMBOLS1)
            count_length += 1
        if self.check_symbols2.isChecked():
            chars.append(SYMBOLS2)
            count_length += 1
        if self.check_symbols3.isChecked():
            chars.append(SYMBOLS3)
            count_length += 1
        if self.check_symbols4.isChecked():
            chars.append(SYMBOLS4)
            count_length += 1
        if self.check_symbols5.isChecked():
            chars.append(SYMBOLS5)
            count_length += 1
        if self.check_symbols6.isChecked():
            chars.append(SYMBOLS6)
            count_length += 1

        if count_length != 0:
            characters = str.join('', chars)
            length = self.slider_password.value() + count_length
            password = pg.PasswordGenerator.create_password(length, characters)
            self.line_generated_password.setText(password)

    def create_passphrase(self):
        word_count = self.slider_passphrase.value()
        seperator = self.combo_passphrase_seperator.currentText()
        font_style = self.combo_passphrase_text.currentIndex()
        dictionary = self.combo_passphrase_lang.currentIndex()
        if dictionary == 0:
            dictionary = DUTCH_DICT
        elif dictionary == 1:
            dictionary = ENGLISH_DICT
        passphrase = pg.PasswordGenerator.dictionary_passphrase(word_count,
                                                                seperator,
                                                                font_style,
                                                                dictionary)
        if self.check_passphrase_numbers.isChecked():
            password = pg.PasswordGenerator.create_password(4, NUMBERS)
            passphrase = passphrase + seperator + password
            self.line_generated_password.setText(passphrase)
        else:
            self.line_generated_password.setText(passphrase)

    def copy_password(self):
        pyperclip.copy(self.line_generated_password.text())
        self.lb_copy_password.setStyleSheet("color: red")
        self.lb_copy_password.setText("Wachtwoord gekopieerd naar klembord")
        start_time = threading.Timer(3, self.set_text_copy)
        start_time.start()

    def set_text_copy(self):
        self.lb_copy_password.setText("")

    def password_slider_value_changed(self):
        slider_value = self.slider_password.value()
        self.spin_password.setValue(slider_value)
        self.create_password()

    def password_spin_value_changed(self):
        spin_value = self.spin_password.value()
        self.slider_password.setValue(spin_value)
        self.create_password()

    def passphrase_slider_value_changed(self):
        slider_value = self.slider_passphrase.value()
        self.spin_passphrase.setValue(slider_value)
        self.create_passphrase()

    def passphrase_spin_value_changed(self):
        spin_value = self.spin_passphrase.value()
        self.slider_passphrase.setValue(spin_value)
        self.create_passphrase()

    def tabwidget_changed(self):
        current_index = self.tabWidget.currentIndex()
        if current_index == 0:
            self.create_password()
        if current_index == 1:
            self.create_passphrase()

    def generate_passsword_button(self):
        current_index = self.tabWidget.currentIndex()
        if current_index == 0:
            self.create_password()
        if current_index == 1:
            self.create_passphrase()

    def check_password_strength(self):
        password_length = len(self.line_generated_password.text())
        if password_length < 6:
            self.progress_password_strength.setValue(20)
            self.progress_password_strength.setStyleSheet(
                "QProgressBar::chunk {background-color: #d72a28;}")
            self.lb_grade.setText("Kwaliteit: Slecht")
        if 6 < password_length < 16:
            self.progress_password_strength.setValue(50)
            self.progress_password_strength.setStyleSheet(
                "QProgressBar::chunk {background-color: #d4a32b;}")
            self.lb_grade.setText("Kwaliteit: Matig")
        if 16 < password_length < 25:
            self.progress_password_strength.setValue(70)
            self.progress_password_strength.setStyleSheet(
                "QProgressBar::chunk {background-color: #bcd728;}")
            self.lb_grade.setText("Kwaliteit: Goed")
        if password_length > 25:
            self.progress_password_strength.setValue(100)
            self.progress_password_strength.setStyleSheet(
                "QProgressBar::chunk {background-color: #78d728;}")
            self.lb_grade.setText("Kwaliteit: Uitstekend")


class InfoWindow(QDialog):
    def __init__(self):
        super().__init__(None, QtCore.Qt.WindowCloseButtonHint)
        loadUi(ui_info_window, self)
        self.setWindowIcon(QtGui.QIcon(icon_app_logo))
        self.setFixedSize(320, 300)
        # Logo
        self.label_info_logo.setText("")
        self.label_info_logo = QLabel(self)
        info_icon = QPixmap(icon_app_logo)
        info_icon = info_icon.scaledToWidth(40)
        self.label_info_logo.setPixmap(info_icon)
        self.label_info_logo.move(140, 20)
        # Labels
        self.label_info_title.setText(f'Password Generator v{current_version}')
        self.label_info_link.setText(
            '<a href="https://github.com/jebr/password-generator">'
            'GitHub repository</a>')
        self.label_info_link.setOpenExternalLinks(True)
        self.label_info_dev.setText('Developers\nJeroen Brauns')
        self.pushButton_update_check.clicked.connect(self.check_update)
        self.lb_update_error.setText("")

    def check_update(self):
        check = bf.BasicFunc.update_check(update_check_url, current_version)
        if check == "no-connection":
            self.lb_update_error.setStyleSheet("color: red")
            self.lb_update_error.setText(
                "Geen internetverbinding<br>Controleren niet mogelijk")
        elif check == "up-to-date":
            self.lb_update_error.setStyleSheet("color: green")
            self.lb_update_error.setText("Je gebruikt de nieuwste versie")
            start_time = threading.Timer(3, self.set_update_text)
            start_time.start()
        else:
            self.close()
            open_update_window(check)

    def set_update_text(self):
        self.lb_update_error.setText("")


class UpdateWindow(QDialog):
    def __init__(self, latest_version):
        super().__init__(None, QtCore.Qt.WindowCloseButtonHint)
        loadUi(ui_update_window, self)
        self.setWindowIcon(QtGui.QIcon(icon_app_logo))
        self.setFixedSize(320, 207)
        # Logo
        self.lb_logo.setText("")
        self.lb_logo = QLabel(self)
        logo_icon = QPixmap(icon_app_logo)
        logo_icon = logo_icon.scaledToWidth(40)
        self.lb_logo.setPixmap(logo_icon)
        self.lb_logo.move(140, 20)
        # Labels
        self.lb_latest_version.setText(f'{latest_version}')
        # Download button
        self.pb_download_new_version.clicked.connect(open_download_link)


def main():
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
