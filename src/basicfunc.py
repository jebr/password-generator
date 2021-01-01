"""
Password Generator Basic Functions
"""

import os
import sys

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass

class BasicFunc:

    @staticmethod
    # Resource path bepalen
    def resource_path(relative_path):
        """ Get absolute path to resource, dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))
        # logging.info('Pyinstaller file location {}'.format(base_path))
        return os.path.join(base_path, relative_path)

