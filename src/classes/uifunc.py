"""
Password generator PyQT UI functions
"""

import pyperclip
from PyQt5.uic.properties import QtWidgets

import basicfunc as bf
import passgen as pg

resource_path = bf.BasicFunc.resource_path

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

class UiFunc:
    def __init__(self):
        super().__init__()

    def create_password(self):
        characters = []
        if self.check_az_capital.isChecked():
            characters.append(A_Z_CAPITAL)

        length = self.slider_password.value()

        password = pg.PasswordGenerator.create_password(length, characters)
        self.line_generated_password.setText(password)

    def create_passphrase(self):
        pass


    def copy_password(self):
        pass

    def get_element_status(self):
        pass