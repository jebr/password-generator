"""
Python script to create GUID code and past it to clipboard
https://docs.microsoft.com/en-us/windows/win32/api/guiddef/ns-guiddef-guid
"""
import pyperclip
import random

_HEXA_BASE = "0123456789ABCDEF"

def create_guid():
    """
    Create hexe code with structure XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    """
    guid_1 = ""
    guid_2 = ""
    guid_3 = ""
    guid_4 = ""
    guid_5 = ""

    for i in range(8):
        char1 = random.choice(_HEXA_BASE)
        guid_1 += char1
    for i in range(4):
        char2 = random.choice(_HEXA_BASE)
        guid_2 += char2
    for i in range(4):
        char3 = random.choice(_HEXA_BASE)
        guid_3 += char3
    for i in range(4):
        char4 = random.choice(_HEXA_BASE)
        guid_4 += char4
    for i in range(12):
        char5 = random.choice(_HEXA_BASE)
        guid_5 += char5

    guid = f"{guid_1}-{guid_2}-{guid_3}-{guid_4}-{guid_5}"

    pyperclip.copy(guid)


def main():
    create_guid()


if __name__ == "__main__":
    main()