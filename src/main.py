import os
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui

from src import basicfunc as bf
from src import uifunc as uf

# Software version
current_version = float(1.0)

# try:
#     os.chdir(os.path.dirname(sys.argv[0]))
# except Exception:
#     pass
#
# def resource_path(relative_path):
#     """ Get absolute path to resource, dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
#     # logging.info('Pyinstaller file location {}'.format(base_path))
#     return os.path.join(base_path, relative_path)

resource_path = bf.BasicFunc.resource_path


# External UI files
ui_main_window = resource_path('resources/ui/main_window.ui')
icon_app_logo = resource_path('icons/password-generator-icon.ico')
# icon_generate_password = resource_path()
# icon_copy_password = resource_path()


class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(ui_main_window, self)
        # self.setFixedSize(900, 850)
        # self.setWindowIcon(QtGui.QIcon(icon_app_logo))
        # Pushbuttons
        # self.pb_generate.clicked.connect(uf.UiFunc.create_password(self.uf))
        # self.pb_copy.clicked.connect(uf.copy_password())
        # Sliders
        # self.slider_passphrase.


def main():
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

