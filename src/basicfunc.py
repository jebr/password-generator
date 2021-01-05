import os
import sys
import requests

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass


class BasicFunc():
    """
    Basic functions for applications
    """
    @staticmethod
    # Resource path bepalen
    def resource_path(relative_path):
        """ Get absolute path to resource, dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.environ.get("_MEIPASS2", os.path.abspath(".."))
        # logging.info('Pyinstaller file location {}'.format(base_path))
        return os.path.join(base_path, relative_path)

    @staticmethod
    def update_check(url, current_version) -> str:
        """
        Function to check float number with raw text file GitHub
        :param url: string
        :param current_version: float
        :return string:
        """
        try:
            resp = requests.get(url, timeout=2)
        except Exception as e:
            return 'no-connection'
        if not resp.ok:
            return 'no-connection'
        latest_version = float(resp.text)
        if latest_version <= current_version:
            return 'up-to-date'
        else:
            return f'v{latest_version}'