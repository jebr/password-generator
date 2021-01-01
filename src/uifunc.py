"""
Password generator PyQT UI functions
"""

import pyperclip

from src import basicfunc as bf
from src import main as qt
from src import passgen as pg

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

class UiFunc(Mainpage):

    def create_password(self):
        characters = []
        if qt.check_az_capital.isChecked():
            characters.append(A_Z_CAPITAL)

        length = qt.slider_password.value()

        password = pg.PasswordGenerator.create_password(length, characters)
        qt.line_generated_password.setText(password)

    def create_passphrase(self):
        pass


    def copy_password(self):
        pass

    def get_element_status(self):
        pass