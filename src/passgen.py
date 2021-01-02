import random
import json


class PasswordGenerator():

    @staticmethod
    def create_password(length, characters) -> str:
        """
        Function to generate a password based on length and caharacters
        :param length: int
        :param characters: string
        :return password: -> string
        """
        password = ""
        for i in range(length):
            char = random.choice(characters)
            password += char
        return password

    @staticmethod
    def dictionary_passphrase(word_count, seperator, font_style,
                                           dictionary) -> str:
        """"
        Function to creata a passphrase based on dictionary words
        :param word_count: int
        :param seperator: string
        :param font_style: int
        :param dictionary: string
        :return str -> passphrase:
        """
        password_words = []
        count = word_count

        with open(dictionary) as w:
            words = json.load(w)

        while count > 0:
            word = random.choice(words)
            if (len(word) < 5) or (len(word) > 5):
                continue
            else:
                password_words.append(word)
                count -= 1

        passphrase = str.join(str(seperator), password_words)

        if font_style == 0:
            return passphrase.lower()
        elif font_style == 1:
            return passphrase.upper()
        elif font_style == 2:
            return passphrase.title()

